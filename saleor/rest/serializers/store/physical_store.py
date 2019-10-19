from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'PhysicalStoreSerializer',
]

PhysicalStore = apps.get_model(*'store.PhysicalStore'.split())


class PhysicalStoreSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`store.PhysicalStore`:

    `**Fields:**`
        01. `address`                     : `ForeignKey` [:model:`account.Address`]
        02. `id`                          : `AutoField`
        03. `is_main_store`               : `BooleanField`
        04. `name`                        : `CharField`
        05. `site`                        : `ForeignKey` [:model:`sites.Site`]

    `**Reverse Fields:**`
        01. `glovo_delivery_permission`   : `OneToOneField` [:model:`glovo.GlovoDeliveryPermission`]
        02. `glovo_order`                  : `ForeignKey` [:model:`glovo.GlovoOrder`]
        03. `phone`                       : `ForeignKey` [:model:`store.Phone`]
    """

    class Meta:
        model = PhysicalStore
        fields = [
            # Fields
            'address',
            'id',
            'is_main_store',
            'name',
            'site',

            # Reverse Fields
            # 'glovo_delivery_permission',
            # 'glovo_order',
            # 'phone',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
