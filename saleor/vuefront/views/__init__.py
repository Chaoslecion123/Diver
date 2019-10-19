# from django.views.generic import TemplateView
from django.shortcuts import redirect, render

STOREFRONT_TEMPLATE = 'app.html'


def anywhere(request, *args, **kwargs):
    return render(request, STOREFRONT_TEMPLATE)


def storefront_index(request, *args, **kwargs):
    return render(request, STOREFRONT_TEMPLATE)
