from django.utils.translation import pgettext_lazy


class ShippingMethodType:
    PRICE_BASED = 'price'
    WEIGHT_BASED = 'weight'
    LOCATION_BASED = 'location'

    CHOICES = [
        (PRICE_BASED, pgettext_lazy(
            'Type of shipping', 'Price based shipping')),
        (WEIGHT_BASED, pgettext_lazy(
            'Type of shipping', 'Weight based shipping')),
        (LOCATION_BASED, pgettext_lazy(
            'Type of shipping', 'Location based shipping'))]
