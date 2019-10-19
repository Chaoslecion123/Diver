from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'FavoriteCollectionSerializer',
]

FavoriteCollection = apps.get_model(*'account.FavoriteCollection'.split())


class FavoriteCollectionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.FavoriteCollection`:

    `**Fields:**`
    01. `user`                    : `ForeignKey` [:model:`account.User`]
    02. `product`                        : `DateTimeField`

    `**Reverse Fields:**`
        01. `product`              : `ManyToManyField` [:model:`product.Product`]
    """
    class Meta:
        model = FavoriteCollection
        fields = [
            'user',
            'product',
        ]
        read_only_fields = []
