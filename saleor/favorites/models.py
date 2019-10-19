from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class FavoriteCollection(models.Model):
    name = models.CharField(
        max_length=255,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='favorite_collections',
        related_query_name='favorite_collection',
        on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='favorites',
        related_query_name='favorite',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        "product.Product",
        related_name='lovers',
        related_query_name='lover',
        on_delete=models.CASCADE,
    )

    collection = models.ForeignKey(
        FavoriteCollection,
        related_name='items',
        related_query_name='item',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('user', 'product')
