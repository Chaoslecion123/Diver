from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ...core.filters import SortedFilterSet
from ...brand.models import Brand

SORT_BY_FIELDS = {
    'name': pgettext_lazy('Brand list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class BrandFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Brand list name filter label', 'Name'),
        lookup_expr='icontains')
    is_featured = ChoiceFilter(
        label=pgettext_lazy('Brand list filter label', 'Is featured'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    sort_by = OrderingFilter(
        label=pgettext_lazy('Brand list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = Brand
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard brands list',
            'Found %(counter)d matching brand',
            'Found %(counter)d matching brands',
            number=counter) % {'counter': counter}
