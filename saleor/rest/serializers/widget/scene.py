from django.apps import apps
from django.conf import settings
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


from .spotlight import SpotlightSerializer


__all__ = [
    'SceneSerializer',
]

Scene = apps.get_model(*'widget.Scene'.split())
Spotlight = apps.get_model(*'widget.Spotlight'.split())


class SceneSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Scene`:

    `**Fields:**`
        01. `active_on`                   : `DateField`
        02. `active_until`                : `DateField`
        03. `alt`                         : `CharField`
        04. `id`                          : `AutoField`
        05. `image`                       : `FileField`
        06. `is_active`                   : `BooleanField`
        07. `name`                        : `CharField`
        08. `ppoi`                        : `CharField`

    `**Reverse Fields:**`
        01. `spotlights`                  : `ForeignKey` [:model:`widget.Spotlight`]
    """
    image = VersatileImageFieldSerializer(
        sizes=settings.VERSATILEIMAGEFIELD_RENDITION_KEY_SETS.get(
            'scene',
            (('original', 'url'), )
        )
    )

    spotlights = serializers.PrimaryKeyRelatedField(
        queryset=Spotlight.objects.all(),
        allow_null=False,
        required=False,
        many=True,
    )

    expandable_fields = {
        'spotlights': (
            SpotlightSerializer, {
                'fields': [
                    'id',
                    'point_x',
                    'point_y',
                    'product'
                ],
                'many': True
            }
        )
    }

    class Meta:
        model = Scene
        fields = [
            # Fields
            'id',
            'alt',
            'name',
            'image',
            # 'ppoi',
            # 'active_on',
            # 'active_until',
            # 'is_active',

            # Reverse Fields
            'spotlights',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
