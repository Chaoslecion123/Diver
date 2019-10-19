from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.translation import pgettext_lazy

from ...core.utils import get_paginator_items
from ...brand.models import Brand
from ..menu.utils import get_menus_that_needs_update, update_menus
from ..views import staff_member_required
from .filters import BrandFilter
from .forms import BrandForm


@staff_member_required
@permission_required('brand.manage_brands')
def brand_list(request):
    brands = Brand.objects.order_by('name')
    brand_filter = BrandFilter(request.GET, queryset=brands)
    brands = get_paginator_items(
        brand_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'))
    ctx = {
        'brands': brands, 'filter_set': brand_filter,
        'is_empty': not brand_filter.queryset.exists()}
    return TemplateResponse(request, 'dashboard/brand/list.html', ctx)


@staff_member_required
@permission_required('brand.manage_brands')
def brand_create(request):
    brand = Brand()
    form = BrandForm(
        request.POST or None, request.FILES or None, instance=brand)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Brand message', 'Added brand')
        messages.success(request, msg)
        return redirect('dashboard:brand-list')
    ctx = {'brand': brand, 'form': form}
    return TemplateResponse(request, 'dashboard/brand/form.html', ctx)


@staff_member_required
@permission_required('brand.manage_brands')
def brand_update(request, pk=None):
    brand = get_object_or_404(Brand, pk=pk)
    form = BrandForm(
        request.POST or None, request.FILES or None, instance=brand)
    if form.is_valid():
        brand = form.save()
        msg = pgettext_lazy('Brand message', 'Updated brand')
        messages.success(request, msg)
        return redirect('dashboard:brand-update', pk=brand.pk)
    ctx = {
        'brand': brand,
        'form': form, }
    return TemplateResponse(request, 'dashboard/brand/form.html', ctx)


@staff_member_required
@permission_required('brand.manage_brands')
def brand_delete(request, pk=None):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        # Needs review
        # menus = get_menus_that_needs_update(brand=brand)
        brand.delete()
        # Needs review
        # if menus:
        #     update_menus(menus)
        msg = pgettext_lazy('Brand message', 'Deleted brand')
        messages.success(request, msg)
        if request.is_ajax():
            response = {'redirectUrl': reverse('dashboard:brand-list')}
            return JsonResponse(response)
        return redirect('dashboard:brand-list')
    ctx = {
        'brand': brand, }
    return TemplateResponse(
        request, 'dashboard/brand/confirm_delete.html', ctx)
