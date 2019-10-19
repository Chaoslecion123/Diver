from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ....core.filters import SortedFilterSet
from ....widget import SliderType
from ....widget.models import Slider


SORT_BY_FIELDS = {
    'name': pgettext_lazy('Brand list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class SliderFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Slider name filter label', 'Name'),
        lookup_expr='icontains')
    type = ChoiceFilter(
        field_name='type',
        label=pgettext_lazy('Slider type filter label', 'Slider type'),
        choices=SliderType.CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    is_active = ChoiceFilter(
        label=pgettext_lazy('Brand list filter label', 'Is public'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    is_default = ChoiceFilter(
        label=pgettext_lazy('Brand list filter label', 'Is default'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    sort_by = OrderingFilter(
        label=pgettext_lazy('Voucher list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = Slider
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard sliders list',
            'Found %(counter)d matching slider',
            'Found %(counter)d matching sliders',
            number=counter) % {'counter': counter}
