from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .user import UserSerializer


__all__ = [
    'ReviewSerializer',
]


Review = apps.get_model(*'reviews.Review'.split())


class ReviewSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.FavoriteCollection`:

    `**Fields:**`
    01. `user`                    : `ForeignKey` [:model:`account.User`]
    02. `product`                 : `ForeignKey` [:model:`product.Product`]
    03. 'comment'                 : 'TextField'
    04. 'score'                   : 'PositiveSmallIntegerField'

    `**Reverse Fields:**`
        01. `product`              : `ManyToManyField` [:model:`product.Product`]
    """
    upvotes = serializers.IntegerField(source='get_upvotes_count', read_only=True)
    downvotes = serializers.IntegerField(source='get_downvotes_count', read_only=True)

    expandable_fields = {
        'user': (
            UserSerializer, {
                'fields': [
                    'email',
                    'first_name',
                    'last_name',
                ]
            }
        )
    }

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'product',
            'score',
            'comment',
            'created',

            # Other fields
            'upvotes',
            'downvotes',
        ]
        read_only_fields = []
