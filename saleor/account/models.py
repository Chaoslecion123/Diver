import uuid

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.db.models import Q, Value
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import pgettext_lazy
from django_countries.fields import Country, CountryField
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from ..geoposition.fields import GeopositionField
from .validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]


class AddressQueryset(models.QuerySet):
    def annotate_default(self, user):
        # Set default shipping/billing address pk to None
        # if default shipping/billing address doesn't exist
        default_shipping_address_pk, default_billing_address_pk = None, None
        if user.default_shipping_address:
            default_shipping_address_pk = user.default_shipping_address.pk
        if user.default_billing_address:
            default_billing_address_pk = user.default_billing_address.pk

        return user.addresses.annotate(
            user_default_shipping_address_pk=Value(
                default_shipping_address_pk, models.IntegerField()),
            user_default_billing_address_pk=Value(
                default_billing_address_pk, models.IntegerField()))


class LocationType:
    HOME = 'home'
    OFFICE = 'office'
    BUILDING = 'building'
    CONDOMINIUM = 'condominium'
    COUNTRY_HOUSE = 'country-house'
    BUSINESSES = 'businesses'
    OTHER = 'other'

    CHOICES = (
        (HOME, pgettext_lazy('Location type home', 'Casa')),
        (OFFICE, pgettext_lazy('Location type office', 'Oficina')),
        (BUILDING, pgettext_lazy('Location type building', 'Edificio')),
        (CONDOMINIUM, pgettext_lazy('Location type condominium', 'Condominio')),
        (COUNTRY_HOUSE, pgettext_lazy('Location type country house', 'Quinta')),
        (BUSINESSES, pgettext_lazy('Location type businesses', 'Negocio')),
        (OTHER, pgettext_lazy('Location type other', 'Otro')),
    )

    MAP = dict(CHOICES)
    LIST = list(MAP.keys())

    def get_label_for(self, value):
        return self.MAP.get(value, f'* Invalid value: {value}')


class Address(models.Model):
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    company_name = models.CharField(max_length=256, blank=True)
    street_address_1 = models.CharField(max_length=256, blank=True)
    street_address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    city_area = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = CountryField()
    country_area = models.CharField(max_length=128, blank=True)
    phone = PossiblePhoneNumberField(blank=True, default='')
    # BEGIN :: SoftButterfly Extensions ----------------------------------------
    position = GeopositionField(blank=True, null=True)
    location_type = models.CharField(
        max_length=256,
        choices=LocationType.CHOICES,
        blank=True,
    )
    country_area_object = models.ForeignKey(
        "world.CountryArea",
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    city_object = models.ForeignKey(
        "world.City",
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    city_area_object = models.ForeignKey(
        "world.CityArea",
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )
    # END :: SoftButterfly Extensions ------------------------------------------

    objects = AddressQueryset.as_manager()

    class Meta:
        ordering = ('pk', )

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        if self.company_name:
            return '%s - %s' % (self.company_name, self.full_name)
        return self.full_name

    def __eq__(self, other):
        # BEGIN :: SoftButterfly Extensions ------------------------------------
        if isinstance(other, type(self)):
            return self.as_data() == other.as_data()

        return False
        # END :: SoftButterfly Extensions --------------------------------------

    __hash__ = models.Model.__hash__

    def as_data(self):
        """Return the address as a dict suitable for passing as kwargs.

        Result does not contain the primary key or an associated user.
        """
        data = model_to_dict(
            self,
            exclude=[
                'id',
                'user',
                'position',
                'location_type',
                'country_area_object',
                'city_object',
                'city_area_object'
            ]
        )
        if isinstance(data['country'], Country):
            data['country'] = data['country'].code
        if isinstance(data['phone'], PhoneNumber):
            data['phone'] = data['phone'].as_e164
        return data

    def get_copy(self):
        """Return a new instance of the same address."""
        return Address.objects.create(**self.as_data())

    @property
    def ubigeo(self):
        if self.city_area_object:
            return self.city_area_object.ubigeo
        return None


class UserManager(BaseUserManager):

    def create_user(
            self, email, password=None, is_staff=False, is_active=True,
            **extra_fields):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop('username', None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff,
            **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields)

    def customers(self):
        return self.get_queryset().filter(
            Q(is_staff=False) | (Q(is_staff=True) & Q(orders__isnull=False)))

    def staff(self):
        return self.get_queryset().filter(is_staff=True)


def get_token():
    return str(uuid.uuid4())


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    addresses = models.ManyToManyField(
        Address, blank=True, related_name='user_addresses')
    is_staff = models.BooleanField(default=False)
    token = models.UUIDField(default=get_token, editable=False, unique=True)
    is_active = models.BooleanField(default=True)
    note = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    default_shipping_address = models.ForeignKey(
        Address, related_name='+', null=True, blank=True,
        on_delete=models.SET_NULL)
    default_billing_address = models.ForeignKey(
        Address, related_name='+', null=True, blank=True,
        on_delete=models.SET_NULL)
    avatar = VersatileImageField(
        upload_to='user-avatars', blank=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        permissions = (
            (
                'manage_users', pgettext_lazy(
                    'Permission description', 'Manage customers.')),
            (
                'manage_staff', pgettext_lazy(
                    'Permission description', 'Manage staff.')),
            (
                'impersonate_users', pgettext_lazy(
                    'Permission description', 'Impersonate customers.')))

    def get_full_name(self):
        if self.first_name or self.last_name:
            return ('%s %s' % (self.first_name, self.last_name)).strip()
        if self.default_billing_address:
            first_name = self.default_billing_address.first_name
            last_name = self.default_billing_address.last_name
            if first_name or last_name:
                return ('%s %s' % (first_name, last_name)).strip()
        return self.email

    def get_short_name(self):
        return self.email

    def get_ajax_label(self):
        address = self.default_billing_address
        if address:
            return '%s %s (%s)' % (
                address.first_name, address.last_name, self.email)
        return self.email

    @property
    def is_subscribed(self):
        if self.pk is None:
            return False

        return self.subscription.is_active  # pylint: disable=no-member

    def get_favorite_products(self):
        from ..product.models import Product

        if self.pk is not None:
            return Product.objects.filter(
                pk__in=self.favorites.values_list('product', flat=True))

        return None

    @property
    def favorite_products(self):
        return self.get_favorite_products()


class CustomerNote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True,
        on_delete=models.SET_NULL)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notes',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('date', )


class NewsletterSubscription(models.Model):
    customer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='suscription',
        on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
