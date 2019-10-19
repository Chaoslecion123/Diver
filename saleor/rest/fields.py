import copy
import json

from prices import Money

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from django_prices import models

from ..geoposition import Geoposition
from ..geoposition.fields import GeopositionField as GeopositionModelField


class TaxedMoneyField(serializers.Field):
    def to_representation(self, value):
        return {
            'net': {
                'amount': value.net.amount,
                'currency': value.net.currency
            },
            'gross': {
                'amount': value.gross.amount,
                'currency': value.gross.currency
            }
        }


class TaxedMoneyRangeField(serializers.Field):
    def to_representation(self, value):
        return {
            'start': TaxedMoneyField().to_representation(value.start),
            'stop': TaxedMoneyField().to_representation(value.stop),
        }


class MoneyField(serializers.Field):
    def to_representation(self, value):
        return {
            'amount': value.amount,
            'currency': value.currency
        }

    def to_internal_value(self, data):
        return Money(**data)


class MeasurementField(serializers.Field):
    def to_representation(self, value):
        return {
            'value': value.value,
            'unit': value.unit
        }


class GeopositionField(serializers.Field):
    def to_representation(self, value):
        if not value:
            return None

        return {
            'lat': float(value.latitude),
            'lng': float(value.longitude)
        }

    def to_internal_value(self, data):
        if not data:
            return None

        data = json.loads(data)

        if not data or data is None:
            return None

        latitude = data['lat']
        longitude = data['lng']

        return Geoposition(latitude, longitude)


SERIALIZER_FIELD_MAPPING = copy.deepcopy(
    FlexFieldsModelSerializer.serializer_field_mapping
)

SERIALIZER_FIELD_MAPPING.update({
    models.MoneyField: MoneyField,
    models.TaxedMoneyField: TaxedMoneyField,
    GeopositionModelField: GeopositionField
})
