from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect

from saleor.product.models import Product, Category, Collection


def product_detail(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    product_id = kwargs.pop('id', None)

    if product_id is None:
        return redirect('app:error-bad-request')

    products = Product.objects.prefetch_related('variants', 'images').all()
    product = get_object_or_404(products, pk=product_id)
    response.status_code = 200
    response.context_data = {
        'product': product
    }

    return response


def category_detail(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    category_id = kwargs.pop('id', None)

    if category_id is None:
        return redirect('app:error-bad-request')

    categories = Category.objects.all()
    category = get_object_or_404(categories, pk=category_id)
    response.status_code = 200
    response.context_data = {
        'category': category
    }

    return response


def collection_detail(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    collection_id = kwargs.pop('id', None)

    if collection_id is None:
        return redirect('app:error-bad-request')

    categories = Collection.objects.all()
    collection = get_object_or_404(categories, pk=collection_id)
    response.status_code = 200
    response.context_data = {
        'collection': collection
    }

    return response


def brand_detail(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    return response
