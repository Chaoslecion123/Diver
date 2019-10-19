from django.apps import apps
from django.conf import settings
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer

__all__ = [
    'BenefitSerializer',
]

Benefit = apps.get_model(*'widget.Benefit'.split())


def get_rendition_keys():
    rendition_keys = getattr(
        settings,
        'VERSATILEIMAGEFIELD_RENDITION_KEY_SETS',
        None
    )

    if rendition_keys is not None:
        rendition_keys = rendition_keys.get('benefits', None)

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


class BenefitSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`widget.Benefit`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `image`                       : `FileField`
        03. `is_active`                   : `BooleanField`
        04. `name`                        : `CharField`
        05. `text`                        : `TextField`

    `**Reverse Fields:**`
        01. `translations`                : `ForeignKey` [:model:`widget.BenefitTranslation`]
    """

    image = VersatileImageFieldSerializer(
        sizes=get_rendition_keys()
    )

    class Meta:
        model = Benefit
        fields = [
            # Fields
            'id',
            'image',
            'is_active',
            'name',
            'text',

            # Reverse Fields
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
