from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ..product import ProductSerializer

__all__ = [
    'SpotlightSerializer',
]

Spotlight = apps.get_model(*'widget.Spotlight'.split())


class SpotlightSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Spotlight`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `point_x`                     : `DecimalField`
        03. `point_y`                     : `DecimalField`
        04. `product`                     : `ForeignKey` [:model:`product.Product`]
        05. `scene`                       : `ForeignKey` [:model:`widget.Scene`]

    `**Reverse Fields:**`
    """
    product = ProductSerializer(
        fields=[
            'id',
            'name',
            'slug',
            'availability',
        ]
    )

    # expandable_fields = {
    #     'product': (
    #         ProductSerializer, {
    #             'fields': [
    #                 'id',
    #                 'name',
    #             ]
    #         }
    #     )
    # }

    class Meta:
        model = Spotlight
        fields = [
            # Fields
            'id',
            'point_x',
            'point_y',
            'product',
            'scene',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
