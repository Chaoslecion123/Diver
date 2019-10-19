from django.db import models
from django_countries.fields import CountryField


class CountryArea(models.Model):
    """Country area model.

    In the peruvian political division this will represent `Departamentos`.
    """
    country = CountryField(
        multiple=False,
        blank=False
    )
    name = models.CharField(
        max_length=256
    )

    def __str__(self):
        return self.name


class City(models.Model):
    """City model.

    In the peruvian political division this will represent `Provincias`.
    """
    country_area = models.ForeignKey(
        CountryArea,
        related_name='cities',
        related_query_name='city',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=256
    )

    def __str__(self):
        return self.name


class CityArea(models.Model):
    """City area model.

    In the peruvian political division this will represent `Distritos`.
    """
    city = models.ForeignKey(
        City,
        related_name='city_areas',
        related_query_name='city_area',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=256
    )
    ubigeo = models.CharField(
        max_length=12,
        blank=True,
    )

    def __str__(self):
        return self.name
