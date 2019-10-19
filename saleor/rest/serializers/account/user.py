from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import is_expanded, FlexFieldsModelSerializer
from .address import AddressSerializer
from ..product import ProductSerializer

__all__ = [
    'UserSerializer',
]

User = apps.get_model(*'account.User'.split())
Address = apps.get_model(*'account.Address'.split())
Product = apps.get_model(*'product.Product'.split())


class UserSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.User`:

    `**Fields:**`
        01. `addresses`                   : `ManyToManyField` [:model:`account.Address`]
        02. `date_joined`                 : `DateTimeField`
        03. `default_billing_address`     : `ForeignKey` [:model:`account.Address`]
        04. `default_shipping_address`    : `ForeignKey` [:model:`account.Address`]
        05. `email`                       : `CharField`
        06. `first_name`                  : `CharField`
        07. `groups`                      : `ManyToManyField` [:model:`auth.Group`]
        08. `id`                          : `AutoField`
        09. `is_active`                   : `BooleanField`
        10. `is_staff`                    : `BooleanField`
        11. `is_superuser`                : `BooleanField`
        12. `last_login`                  : `DateTimeField`
        13. `last_name`                   : `CharField`
        14. `note`                        : `TextField`
        15. `password`                    : `CharField`
        16. `token`                       : `UUIDField`
        17. `user_permissions`            : `ManyToManyField` [:model:`auth.Permission`]

    `**Reverse Fields:**`
        01. `auth_token`                  : `OneToOneField` [:model:`authtoken.Token`]
        02. `checkouts`                       : `ForeignKey` [:model:`checkout.Checkout`]
        03. `customernote`                : `ForeignKey` [:model:`account.CustomerNote`]
        04. `impersonated_by`             : `ForeignKey` [:model:`impersonate.ImpersonationLog`]
        05. `impersonations`              : `ForeignKey` [:model:`impersonate.ImpersonationLog`]
        06. `logentry`                    : `ForeignKey` [:model:`admin.LogEntry`]
        07. `notes`                       : `ForeignKey` [:model:`account.CustomerNote`]
        08. `orders`                      : `ForeignKey` [:model:`order.Order`]
        09. `social_auth`                 : `ForeignKey` [:model:`social_django.UserSocialAuth`]
    """
    addresses = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        allow_null=True,
        required=False,
        many=True,
    )

    favorite_products = serializers.SerializerMethodField()

    expandable_fields = {
        'addresses': (
            AddressSerializer, {
                'fields': [
                    'id',
                    'company_name',
                    'full_name_addres',
                    'street_address_1',
                    'street_address_2',
                ],
                'many': True
            }
        )
    }

    class Meta:
        model = User
        fields = [
            # Fields
            'addresses',
            'date_joined',
            'default_billing_address',
            'default_shipping_address',
            'email',
            'first_name',
            'groups',
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'last_name',
            'note',
            # 'password',
            # 'token',
            'user_permissions',

            # Reverse Fields
            # 'auth_token',
            # 'checkouts',
            # 'customernote',
            # 'impersonated_by',
            # 'impersonations',
            # 'logentry',
            # 'notes',
            # 'orders',
            # 'social_auth',
            'favorite_products'
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_favorite_products(self, obj):
        request = self.context.get('request', None)
        is_favorite_products_expanded = False

        if request:
            is_favorite_products_expanded = is_expanded(
                request, 'favorite_products')

        if is_favorite_products_expanded:
            return ProductSerializer(
                Product
                .objects
                .filter(
                    pk__in=obj
                    .favorites
                    .values_list(
                        'product',
                        flat=True
                    )
                ),
                many=True
            ).data

        return obj.favorites.values_list('product_id', flat=True)
