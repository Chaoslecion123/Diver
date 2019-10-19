from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import pgettext_lazy

from ....core.utils import get_paginator_items
from ....widget.models import Banner
from ...views import staff_member_required
from .filters import BannerFilter
from . import forms


@staff_member_required
@permission_required('site.manage_settings')
def banner_list(request):
    banners = Banner.objects.all()
    banner_filter = BannerFilter(request.GET, queryset=banners)
    banners = get_paginator_items(
        banner_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'), )

    ctx = {
        'banners': banners,
        'filter_set': banner_filter,
        'is_empty': not banner_filter.queryset.exists()}

    return TemplateResponse(
        request,
        'dashboard/widget/banner/list.html',
        ctx, )


# @staff_member_required
# @permission_required('site.manage_settings')
# def banner_details(request, pk):
#     banner = get_object_or_404(Banner, pk=pk)
#     ctx = {
#         'banner': banner
#     }
#     return TemplateResponse(
#         request,
#         'dashboard/widget/banner/detail.html',
#         ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def banner_create(request):
    banner = Banner()
    form = forms.BannerForm(
        request.POST or None,
        request.FILES or None,
        instance=banner, )

    if form.is_valid():
        banner = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Nuevo banner añadido'), )

        return redirect('dashboard:banner-list')

    ctx = {
        'banner': banner,
        'form': form, }

    return TemplateResponse(
        request,
        'dashboard/widget/banner/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def banner_edit(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    form = forms.BannerForm(
        request.POST or None,
        request.FILES or None,
        instance=banner, )
    if form.is_valid():
        banner = form.save()
        msg = pgettext_lazy('Dashboard message', 'Banner actualizado')
        messages.success(request, msg)
        return redirect('dashboard:banner-list')
    ctx = {
        'banner': banner,
        'form': form
    }

    return TemplateResponse(
        request,
        'dashboard/widget/banner/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Banner eliminado %s') % (banner.name,)
        messages.success(
            request,
            msg, )
        return redirect('dashboard:banner-list')

    ctx = {
        'banner': banner, }
    return TemplateResponse(
        request,
        'dashboard/widget/banner/modal/confirm_delete.html',
        ctx
    )
