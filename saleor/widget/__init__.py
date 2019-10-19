from django.utils.translation import pgettext_lazy


class SliderType:
    HOMEPAGE = 'homepage'
    COLLECTION = 'collection'
    CATEGORY = 'category'
    BRAND = 'brand'

    CHOICES = [
        (HOMEPAGE, pgettext_lazy(
            'Slider type for storefront home page', 'Home page')),
        (COLLECTION, pgettext_lazy(
            'Slider type for storefront collections pages', 'Collections')),
        (CATEGORY, pgettext_lazy(
            'Slider type for storefront categories pages', 'Categories')),
        (BRAND, pgettext_lazy(
            'Slider type for storefront brands pages', 'Brands'))
    ]
