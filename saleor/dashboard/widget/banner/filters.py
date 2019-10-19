from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ....core.filters import SortedFilterSet
from ....widget.models import Banner


SORT_BY_FIELDS = {
    'name': pgettext_lazy('Banner list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class BannerFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Banner name filter label', 'Name'),
        lookup_expr='icontains')
    is_active = ChoiceFilter(
        label=pgettext_lazy('Banner list filter label', 'Is public'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    is_default = ChoiceFilter(
        label=pgettext_lazy('Banner list filter label', 'Is default'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    sort_by = OrderingFilter(
        label=pgettext_lazy('Voucher list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = Banner
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard banners list',
            'Found %(counter)d matching banner',
            'Found %(counter)d matching banners',
            number=counter) % {'counter': counter}
