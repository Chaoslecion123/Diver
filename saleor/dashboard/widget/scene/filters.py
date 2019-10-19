from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ....core.filters import SortedFilterSet
from ....widget.models import Scene


SORT_BY_FIELDS = {
    'name': pgettext_lazy('Scene list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class SceneFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Scene name filter label', 'Name'),
        lookup_expr='icontains')
    is_active = ChoiceFilter(
        label=pgettext_lazy('Scene list filter label', 'Is public'),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    sort_by = OrderingFilter(
        label=pgettext_lazy('Voucher list sorting filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = Scene
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard scenes list',
            'Found %(counter)d matching scene',
            'Found %(counter)d matching scenes',
            number=counter) % {'counter': counter}
