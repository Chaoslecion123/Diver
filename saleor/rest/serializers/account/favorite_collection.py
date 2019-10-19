from django.apps import apps
# from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .favorite import FavoriteSerializer
from .user import UserSerializer


__all__ = [
    'FavoriteCollectionSerializer',
]

Favorite = apps.get_model(*'favorites.Favorite'.split())
FavoriteCollection = apps.get_model(*'favorites.FavoriteCollection'.split())


class FavoriteCollectionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.FavoriteCollectionCollection`:

    `**Fields:**`
    01. `user`                    : `ForeignKey` [:model:`account.User`]
    02. `product`                 : `ForeignKey` [:model:`product.Product`]
    03. 'comment'                 : 'TextField'
    04. 'score'                   : 'PositiveSmallIntegerField'

    `**Reverse Fields:**`
        01. `product`              : `ManyToManyField` [:model:`product.Product`]
    """
    # items = serializers.SlugRelatedField(
    #     queryset=Favorite.objects.all(),
    #     slug_field='uuid',
    #     allow_null=False,
    #     required=False,
    #     many=True,
    # )

    expandable_fields = {
        'user': (
            UserSerializer, {
                'fields': [
                    'email',
                    'first_name',
                    'last_name',
                ]
            }
        ),
        'items': (
            FavoriteSerializer, {
                'many': True,
                'fields': [
                    'id',
                    'name',
                    'slug',
                    'images',
                ]
            }
        )
    }

    class Meta:
        model = FavoriteCollection
        fields = [
            'id',
            'name',
            'user',

            # Other fields
            'items',
        ]
        read_only_fields = []
