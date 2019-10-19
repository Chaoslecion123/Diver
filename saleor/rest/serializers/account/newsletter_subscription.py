from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'NewsletterSubscriptionSerializer',
]

NewsletterSubscription = apps.get_model(*'account.NewsletterSubscription'.split())


class NewsletterSubscriptionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.NewsletterSubscription`:

    `**Fields:**`
        01. `customer`                    : `OneToOneField` [:model:`account.User`]
        02. `email`                       : `CharField`
        03. `id`                          : `AutoField`
        04. `is_active`                   : `BooleanField`

    `**Reverse Fields:**`
    """

    class Meta:
        model = NewsletterSubscription
        fields = [
            # Fields
            'customer',
            'email',
            'id',
            'is_active',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
