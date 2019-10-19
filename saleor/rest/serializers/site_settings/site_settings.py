from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ..store.footer_item import FooterItemSerializer
from ..store.bank_account import BankAccountSerializer
from ..store.social_network import SocialNetworkSerializer
from ..store.special_page import SpecialPageSerializer
from .authorization_key import AuthorizationKeySerializer


__all__ = [
    'SiteSettingsSerializer',
]

SiteSettings = apps.get_model(*'site.SiteSettings'.split())


class SiteSettingsSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`site.SiteSettings`:

    `**Fields:**`
        01. `automatic_fulfillment_digital_products`: `BooleanField`
        02. `bottom_menu`                 : `ForeignKey` [:model:`menu.Menu`]
        03. `cash_payment_enabled`        : `BooleanField`
        04. `charge_taxes_on_shipping`    : `BooleanField`
        05. `dashboard_button_color`      : `CharField`
        06. `dashboard_header_color`      : `CharField`
        07. `dashboard_header_text_color` : `CharField`
        08. `dashboard_logo`              : `FileField`
        09. `dashboard_subheader_color`   : `CharField`
        10. `default_digital_max_downloads`: `IntegerField`
        11. `default_digital_url_valid_days`: `IntegerField`
        12. `default_weight_unit`         : `CharField`
        13. `description`                 : `CharField`
        14. `display_gross_prices`        : `BooleanField`
        15. `header_text`                 : `CharField`
        16. `homepage_collection`         : `ForeignKey` [:model:`product.Collection`]
        17. `id`                          : `AutoField`
        18. `include_taxes_in_prices`     : `BooleanField`
        19. `payment_against_delivery_enabled`: `BooleanField`
        20. `site`                        : `OneToOneField` [:model:`sites.Site`]
        21. `store_accent_color`          : `CharField`
        22. `store_header_color`          : `CharField`
        23. `store_header_text_color`     : `CharField`
        24. `store_logo`                  : `FileField`
        25. `top_menu`                    : `ForeignKey` [:model:`menu.Menu`]
        26. `track_inventory_by_default`  : `BooleanField`

    `**Reverse Fields:**`
        01. `authorizationkey`            : `ForeignKey` [:model:`site.AuthorizationKey`]
        02. `bank_account`                : `ForeignKey` [:model:`store.BankAccount`]
        03. `footer_items`                : `ForeignKey` [:model:`store.FooterItem`]
        04. `social_network`              : `ForeignKey` [:model:`store.SocialNetwork`]
        05. `special_page`                : `ForeignKey` [:model:`store.SpecialPage`]
        06. `translations`                : `ForeignKey` [:model:`site.SiteSettingsTranslation`]
    """
    authorizationkey_set = AuthorizationKeySerializer(many=True, fields=['key', 'name'])
    bank_accounts = BankAccountSerializer(many=True, fields=['number', 'provider', ])
    footer_items = FooterItemSerializer(many=True, fields=['sort_order', 'menu', ])
    social_networks = SocialNetworkSerializer(many=True, fields=['link', 'provider', ])
    special_pages = SpecialPageSerializer(many=True, fields=['type', 'pagez', ])

    class Meta:
        model = SiteSettings
        fields = [
            # Fields
            'automatic_fulfillment_digital_products',
            'bottom_menu',
            'cash_payment_enabled',
            'charge_taxes_on_shipping',
            'dashboard_button_color',
            'dashboard_header_color',
            'dashboard_header_text_color',
            'dashboard_logo',
            'dashboard_subheader_color',
            'default_digital_max_downloads',
            'default_digital_url_valid_days',
            'default_weight_unit',
            'description',
            'display_gross_prices',
            'header_text',
            'homepage_collection',
            'id',
            'include_taxes_in_prices',
            'payment_against_delivery_enabled',
            'site',
            'store_accent_color',
            'store_header_color',
            'store_header_text_color',
            'store_logo',
            'top_menu',
            'track_inventory_by_default',

            # Reverse Fields
            'authorizationkey_set',
            'bank_accounts',
            'footer_items',
            'social_networks',
            'special_pages',
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
