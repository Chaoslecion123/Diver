from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import pgettext_lazy

from ....core.utils import get_paginator_items
from ....widget.models import Benefit
from ...views import staff_member_required
from .filters import BenefitFilter
from . import forms


@staff_member_required
@permission_required('site.manage_settings')
def benefit_list(request):
    benefits = Benefit.objects.all()
    benefit_filter = BenefitFilter(request.GET, queryset=benefits)
    benefits = get_paginator_items(
        benefit_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'), )

    ctx = {
        'benefits': benefits,
        'filter_set': benefit_filter,
        'is_empty': not benefit_filter.queryset.exists()}

    return TemplateResponse(
        request,
        'dashboard/widget/benefit/list.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def benefit_create(request):
    benefit = Benefit()
    form = forms.BenefitForm(
        request.POST or None,
        request.FILES or None,
        instance=benefit, )

    if form.is_valid():
        benefit = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Nuevo benefit añadido'), )

        return redirect('dashboard:benefit-list')

    ctx = {
        'benefit': benefit,
        'form': form, }

    return TemplateResponse(
        request,
        'dashboard/widget/benefit/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def benefit_edit(request, pk):
    benefit = get_object_or_404(Benefit, pk=pk)
    form = forms.BenefitForm(
        request.POST or None,
        request.FILES or None,
        instance=benefit, )
    if form.is_valid():
        benefit = form.save()
        msg = pgettext_lazy('Dashboard message', 'Benefit actualizado')
        messages.success(request, msg)
        return redirect('dashboard:benefit-list')
    ctx = {
        'benefit': benefit,
        'form': form
    }

    return TemplateResponse(
        request,
        'dashboard/widget/benefit/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def benefit_delete(request, pk):
    benefit = get_object_or_404(Benefit, pk=pk)
    if request.method == 'POST':
        benefit.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Benefit eliminado %s') % (benefit.name,)
        messages.success(
            request,
            msg, )
        return redirect('dashboard:benefit-list')

    ctx = {
        'benefit': benefit, }
    return TemplateResponse(
        request,
        'dashboard/widget/benefit/modal/confirm_delete.html',
        ctx
    )
