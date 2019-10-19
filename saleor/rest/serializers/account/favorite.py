from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ..product import ProductSerializer
from .user import UserSerializer


__all__ = [
    'FavoriteSerializer',
]

Favorite = apps.get_model(*'favorites.Favorite'.split())


class FavoriteSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.FavoriteCollection`:

    `**Fields:**`
    01. `user`                    : `ForeignKey` [:model:`account.User`]
    02. `product`                 : `ForeignKey` [:model:`product.Product`]
    03. 'comment'                 : 'TextField'
    04. 'score'                   : 'PositiveSmallIntegerField'

    `**Reverse Fields:**`
        01. `product`              : `ManyToManyField` [:model:`product.Product`]
    """
    expandable_fields = {
        'user': (
            UserSerializer, {
                'fields': [
                    'id',
                    'email',
                    'first_name',
                    'last_name',
                ]
            }
        ),
        'product': (
            ProductSerializer, {
                'fields': [
                    'id',
                    'name',
                    'slug',
                    'image',
                ]
            }
        )
    }

    class Meta:
        model = Favorite
        fields = [
            'id',
            'user',
            'product',
            'collection',
            'created',
        ]
        read_only_fields = []
