from django.apps import apps
from django.conf import settings
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


__all__ = [
    'SlideSerializer',
]

Slide = apps.get_model(*'widget.Slide'.split())


def get_rendition_keys():
    rendition_keys = getattr(
        settings,
        'VERSATILEIMAGEFIELD_RENDITION_KEY_SETS',
        None
    )

    if rendition_keys is not None:
        rendition_keys = rendition_keys.get('slides', None)

    if rendition_keys is None:
        return [
            ("small", "thumbnail__110x45"),
            ("small_2x", "thumbnail__220x90"),
            ("medium", "thumbnail__330x135"),
            ("medium_2x", "thumbnail__660x270"),
            ("large", "thumbnail__800x360"),
            ("large_2x", "thumbnail__1760x720"),
        ]

    return rendition_keys


class SlideSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Slide`:

    `**Fields:**`
        01. `alt`                         : `CharField`
        02. `id`                          : `AutoField`
        03. `image`                       : `FileField`
        04. `ppoi`                        : `CharField`
        05. `slider`                      : `ForeignKey` [:model:`widget.Slider`]
        06. `sort_order`                  : `PositiveIntegerField`

    `**Reverse Fields:**`
    """
    image = VersatileImageFieldSerializer(
        sizes=get_rendition_keys()
    )

    class Meta:
        model = Slide
        fields = [
            # Fields
            'alt',
            'id',
            'image',
            # 'ppoi',
            'slider',
            'sort_order',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
