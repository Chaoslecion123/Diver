from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ....core.filters import SortedFilterSet
from ....store.models import PhysicalStore


SORT_BY_FIELDS = {
    'name': pgettext_lazy('Physical store list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class PhysicalStoreFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Physical store name filter label', 'Name'),
        lookup_expr='icontains')
    is_main_store = ChoiceFilter(
        label=pgettext_lazy('Physical store list filter label', 'Principal'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    sort_by = OrderingFilter(
        label=pgettext_lazy(
            'Physical store list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = PhysicalStore
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard physical store list',
            'Found %(counter)d matching physical store',
            'Found %(counter)d matching physical stores',
            number=counter) % {'counter': counter}
