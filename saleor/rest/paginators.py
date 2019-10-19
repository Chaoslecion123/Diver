from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings


__all__ = [
    'DynamicPageNumberPagination'
]


class DynamicPageNumberPagination(PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    max_page_size = 1000

    page_query_param = 'page'
    page_query_description = _(
        'A page number within the paginated result set.')

    page_size_query_param = 'page_size'
    page_size_query_description = _('Number of results to return per page.')

    last_page_strings = ('last',)
    invalid_page_message = _('Invalid page.')

    def get_paginated_response(self, data):
        objects_count = self.page.paginator.count
        pages_count = self.page.paginator.num_pages
        current_page = self.page.number
        previous_page = None

        if self.page.has_previous():
            previous_page = self.page.previous_page_number()

        next_page = None
        if self.page.has_next():
            next_page = self.page.next_page_number()

        return Response(OrderedDict([
            ('meta', OrderedDict([
                ('count', objects_count),
                ('previous', previous_page),
                ('current', current_page),
                ('next', next_page),
                ('pages', pages_count),
            ])),
            ('items', data)
        ]))
