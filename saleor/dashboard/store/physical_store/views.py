from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import pgettext_lazy
from django.contrib.sites.shortcuts import get_current_site

from ....core.utils import get_paginator_items
from ....account.models import Address
from ....glovo.models import GlovoDeliveryPermission
from ....runningbox.models import RunningBoxDeliveryPermission
from ....store.models import PhysicalStore
from ...views import staff_member_required
from .filters import PhysicalStoreFilter
from . import forms


@staff_member_required
@permission_required('store.manage_physical_stores')
def physical_store_list(request):
    site = get_current_site(request)
    physical_stores = site.physical_stores.all()
    physical_store_filter = PhysicalStoreFilter(
        request.GET, queryset=physical_stores)
    physical_stores = get_paginator_items(
        physical_store_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'), )

    ctx = {
        'physical_stores': physical_stores,
        'filter_set': physical_store_filter,
        'is_empty': not physical_store_filter.queryset.exists()
    }

    return TemplateResponse(
        request,
        'dashboard/store/physical_store/list.html',
        ctx,
    )


# @staff_member_required
# @permission_required('store.manage_physical_stores')
# def physical_store_details(request, pk):
#     physical_store = get_object_or_404(PhysicalStore, pk=pk)
#     ctx = {
#         'physical_store': physical_store
#     }
#     return TemplateResponse(
#         request,
#         'dashboard/store/physical_store/detail.html',
#         ctx, )


@staff_member_required
@permission_required('store.manage_physical_stores')
def physical_store_create(request):
    site = get_current_site(request)
    physical_store = PhysicalStore()
    physical_store.site = site
    physical_store_form = forms.PhysicalStoreForm(
        request.POST or None,
        request.FILES or None,
        instance=physical_store,
    )
    address_form = forms.AddressForm(
        request.POST or None,
        request.FILES or None,
        initial={'country': request.country},
        instance=Address(),
    )
    glovo_delivery_permission_form = forms.GlovoDeliveryPermissionForm(
        request.POST or None,
        request.FILES or None,
        instance=GlovoDeliveryPermission(),
    )
    runningbox_delivery_permission_form = forms.RunningBoxDeliveryPermissionForm(
        request.POST or None,
        request.FILES or None,
        instance=RunningBoxDeliveryPermission(),
    )

    if address_form.is_valid() and physical_store_form.is_valid() and glovo_delivery_permission_form.is_valid() and runningbox_delivery_permission_form.is_valid():
        address = address_form.save()
        physical_store_form.instance.address = address
        physical_store = physical_store_form.save()
        address.company_name = physical_store.name
        address.save()
        glovo_delivery_permission_form.instance.store = physical_store
        glovo_delivery_permission_form.save()
        runningbox_delivery_permission_form.instance.store = physical_store
        runningbox_delivery_permission_form.save()

        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Added physical stores'), )

        return redirect('dashboard:physical-store-list')

    ctx = {
        'physical_store': physical_store,
        'physical_store_form': physical_store_form,
        'address_form': address_form,
        'glovo_delivery_permission_form': glovo_delivery_permission_form,
        'runningbox_delivery_permission_form': runningbox_delivery_permission_form,
    }

    return TemplateResponse(
        request,
        'dashboard/store/physical_store/form.html',
        ctx, )


@staff_member_required
@permission_required('store.manage_physical_stores')
def physical_store_edit(request, pk):
    physical_store = get_object_or_404(PhysicalStore, pk=pk)
    physical_store_form = forms.PhysicalStoreForm(
        request.POST or None,
        request.FILES or None,
        instance=physical_store,
    )
    address_form = forms.AddressForm(
        request.POST or None,
        request.FILES or None,
        initial={'country': request.country},
        instance=physical_store.address,
    )
    glovo_delivery_permission_form = forms.GlovoDeliveryPermissionForm(
        request.POST or None,
        request.FILES or None,
        instance=getattr(
            physical_store, 'glovo_delivery_permission', GlovoDeliveryPermission()),
    )
    runningbox_delivery_permission_form = forms.RunningBoxDeliveryPermissionForm(
        request.POST or None,
        request.FILES or None,
        instance=getattr(
            physical_store, 'runningbox_delivery_permission', RunningBoxDeliveryPermission()),
    )
    if address_form.is_valid() and physical_store_form.is_valid() and glovo_delivery_permission_form.is_valid() and runningbox_delivery_permission_form.is_valid():
        address = address_form.save()
        physical_store_form.instance.address = address
        physical_store = physical_store_form.save()
        address.company_name = physical_store.name
        address.save()
        glovo_delivery_permission_form.instance.store = physical_store
        glovo_delivery_permission_form.save()
        runningbox_delivery_permission_form.instance.store = physical_store
        runningbox_delivery_permission_form.save()

        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Added physical stores'), )

        return redirect('dashboard:physical-store-list')

    ctx = {
        'physical_store': physical_store,
        'physical_store_form': physical_store_form,
        'address_form': address_form,
        'glovo_delivery_permission_form': glovo_delivery_permission_form,
        'runningbox_delivery_permission_form': runningbox_delivery_permission_form,
    }

    return TemplateResponse(
        request,
        'dashboard/store/physical_store/form.html',
        ctx, )


@staff_member_required
@permission_required('store.manage_physical_stores')
def physical_store_delete(request, pk):
    physical_store = get_object_or_404(PhysicalStore, pk=pk)
    if request.method == 'POST':
        physical_store.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Deleted physical store %s') % (physical_store.name,)
        messages.success(
            request,
            msg, )
        return redirect('dashboard:physical-store-list')

    ctx = {
        'physical_store': physical_store, }
    return TemplateResponse(
        request,
        'dashboard/store/physical_store/modal/confirm_delete.html',
        ctx
    )
