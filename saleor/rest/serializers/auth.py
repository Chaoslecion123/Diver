import copy
import logging

from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation as validators
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm as LegacyPasswordResetForm
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.encoding import force_text
from django.contrib.auth.forms import SetPasswordForm

from rest_framework import serializers
from rest_framework import serializers
from rest_framework import exceptions
from rest_auth.serializers import PasswordResetSerializer as LegacyPasswordResetSerializer
from rest_flex_fields import is_expanded, FlexFieldsModelSerializer

from saleor.account.emails import send_password_reset_email
from saleor.account.models import NewsletterSubscription

from .account.address import AddressSerializer
from .product.product import ProductSerializer


__all__ = [
    'LoginSerializer',
    'UserDetailSerializer'
]

logger = logging.getLogger(__name__)

# The correct way to get the user model from django config
# altought we now that get_user_mode will return our BssUser model
USER_MODEL = get_user_model()
Address = apps.get_model(*'account.Address'.split())
Product = apps.get_model(*'product.Product'.split())


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    suscribed_to_newsletter = serializers.BooleanField(write_only=True)
    terms_and_conditions = serializers.BooleanField(write_only=True)

    def validate_email(self, email):
        if email and USER_MODEL.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address.")
            )

        return email

    def validate_terms_and_conditions(self, terms_and_conditions):
        if not terms_and_conditions:
            raise serializers.ValidationError(
                _("¡Debes estar de acuerdo para continuar!")
            )

        return terms_and_conditions

    def validate(self, data):
        data_to_validate = copy.deepcopy(data)
        password = data_to_validate.pop('password', None)
        password_confirm = data_to_validate.pop('password_confirm', None)

        # Check password confirm
        if password != password_confirm:
            raise serializers.ValidationError({
                'password': [
                    _("The two password fields didn't match.")
                ]
            })

        suscribed_to_newsletter = data_to_validate.pop(
            'suscribed_to_newsletter', None)

        data_to_validate.pop('terms_and_conditions', None)
        user = USER_MODEL(**data_to_validate)

        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({
                'password': e.messages
            })

        return super().validate(data)

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'suscribed_to_newsletter': self.validated_data.get('suscribed_to_newsletter', False),
        }

    # def save(self, **kwargs):
    def save(self, request):
        data = self.get_cleaned_data()
        password = data.pop('password', '')
        suscribed_to_newsletter = data.pop(
            'suscribed_to_newsletter', None)

        user = USER_MODEL(**data)
        user.set_password(password)
        user.save()

        subscription = NewsletterSubscription.objects.filter(email=user.email)

        if subscription.exists():
            subscription = subscription[0]
            subscription.customer = user
            subscription.is_active = suscribed_to_newsletter
            subscription.save()
        else:
            subscription = NewsletterSubscription(
                customer=user,
                email=user.email,
                is_active=suscribed_to_newsletter,
            )
            subscription.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        # Authentication without using allauth
        if email:
            user = authenticate(
                self.context['request'], email=email, password=password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user

        return attrs


class UserDetailSerializer(FlexFieldsModelSerializer):
    """User model without password"""
    # groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    # groups = GroupSerializer(required=False, many=True)
    # user_permissions = PermissionSerializer(required=False, many=True)
    addresses = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        allow_null=True,
        required=False,
        many=True,
    )

    full_name = serializers.CharField(source="get_full_name", read_only=True)
    # password = serializers.CharField(write_only=True)
    # favorite_products = serializers.SerializerMethodField()
    favorite_products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='get_favorite_products',
        allow_null=False,
        required=False,
        many=True,
    )

    expandable_fields = {
        'favorite_products': (
            ProductSerializer, {
                'fields': [
                    'id',
                    'name',
                    'slug',
                    'image',
                    'availability',
                    'brand'
                ],
                'many': True
            }
        )
    }

    class Meta:
        model = USER_MODEL
        fields = [
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_anonymous',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'groups',
            'full_name',
            'default_billing_address',
            'default_shipping_address',

            # 'favorite_collection',
            # 'review',
            'addresses',
            'favorite_products',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class PasswordResetForm(LegacyPasswordResetForm):
    def get_users(self, email):  # pylint : disable = R0201
        active_users = USER_MODEL.objects.filter(
            email__iexact=email,
            is_active=True)
        return active_users

    def send_mail(  # pylint: disable = R0913
            self, subject_template_name, email_template_name, context,
            from_email, to_email, html_email_template_name=None):
        # Passing the user object to the Celery task throws an
        # error "'User' is not JSON serializable". Since it's not used in our
        # template, we remove it from the context.
        context['user_name'] = context['user'].get_short_name()
        del context['user']
        # print("*** *** ***")
        # print("*** send_password_reset_email ***")
        # print(context)
        # print("*** *** ***")
        # send_password_reset_email(context, to_email)
        send_password_reset_email.delay(context, to_email)


class PasswordResetSerializer(LegacyPasswordResetSerializer):
    password_reset_form_class = PasswordResetForm

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'email_template_name': 'bss/email/password_reset.html',
            'request': request,
        }
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    set_password_form_class = SetPasswordForm
    set_password_form = None
    user = None
    _errors = {}

    new_password_1 = serializers.CharField(max_length=128)
    new_password_2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = USER_MODEL.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, USER_MODEL.DoesNotExist):
            raise exceptions.ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data={
                'new_password1': attrs['new_password_1'],
                'new_password2': attrs['new_password_2'],
                'token': attrs['token'],
                'uid': attrs['uid'],
            }
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        if not default_token_generator.check_token(self.user, attrs['token']):
            raise exceptions.ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ
        return self.set_password_form.save()
