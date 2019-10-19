from django import forms
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from ....core.filters import SortedFilterSet
from ....widget.models import Benefit


SORT_BY_FIELDS = {
    'name': pgettext_lazy('Benefit list sorting option', 'name')}

BOOLEAN_CHOICES = (
    ('1', pgettext_lazy('Is active filter choice', 'Yes')),
    ('0', pgettext_lazy('Is active filter choice', 'No')))


class BenefitFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy(
            'Benefit name filter label',
            'Name'
        ),
        lookup_expr='icontains'
    )
    is_active = ChoiceFilter(
        label=pgettext_lazy(
            'Benefit list filter label',
            'Activo'
        ),
        choices=BOOLEAN_CHOICES,
        empty_label=pgettext_lazy(
            'Filter empty choice label',
            'Todos'
        ),
        widget=forms.Select
    )

    class Meta:
        model = Benefit
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard benefits list',
            'Found %(counter)d matching benefit',
            'Found %(counter)d matching benefits',
            number=counter) % {'counter': counter}
