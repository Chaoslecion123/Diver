from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from ....core.utils import get_paginator_items
from ....widget.models import Slider, Slide
from ....widget import SliderType
from ...views import staff_member_required
from .filters import SliderFilter
from .forms import (
    SliderForm, CollectionSliderForm, CategorySliderForm, BrandSliderForm,
    SlideForm, ReorderSlideForm)


def get_slider_type_forms(slider, data):
    """Return a dict of specific slider type forms."""
    return {
        SliderType.COLLECTION: CollectionSliderForm(
            data or None, instance=slider, prefix=SliderType.COLLECTION),
        SliderType.CATEGORY: CategorySliderForm(
            data or None, instance=slider, prefix=SliderType.CATEGORY),
        SliderType.BRAND: BrandSliderForm(
            data or None, instance=slider, prefix=SliderType.BRAND), }


@staff_member_required
@permission_required('widget.manage_sliders')
def slider_list(request):
    sliders = Slider\
        .objects\
        .prefetch_related('collections', 'categories', 'brands')\
        .order_by()
    slider_filter = SliderFilter(request.GET, queryset=sliders)
    sliders = get_paginator_items(
        slider_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'))
    ctx = {
        'sliders': sliders, 'filter_set': slider_filter,
        'is_empty': not slider_filter.queryset.exists()}
    return TemplateResponse(request, 'dashboard/widget/slider/list.html', ctx)


@staff_member_required
@permission_required('widget.manage_sliders')
def slider_detail(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    ctx = {'slider': slider}
    return TemplateResponse(
        request,
        'dashboard/widget/slider/detail.html',
        ctx, )


@staff_member_required
@permission_required('widget.manage_sliders')
def slider_add(request):
    slider = Slider()
    type_base_forms = get_slider_type_forms(slider, request.POST)
    slider_form = SliderForm(request.POST or None, instance=slider)
    if slider_form.is_valid():
        slider_type = slider_form.cleaned_data.get('type')
        form_type = type_base_forms.get(slider_type)

        if form_type is None:
            slider = slider_form.save()
        elif form_type.is_valid():
            slider = form_type.save()

        if form_type is None or form_type.is_valid():
            msg = pgettext_lazy('Slider message', 'Added slider')
            messages.success(request, msg)
            return redirect('dashboard:slider-list')
    ctx = {
        'slider': slider,
        'form': slider_form,
        'type_base_forms': type_base_forms, }
    return TemplateResponse(
        request, 'dashboard/widget/slider/form.html', ctx)


@staff_member_required
@permission_required('widget.manage_sliders')
def slider_edit(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    type_base_forms = get_slider_type_forms(slider, request.POST)
    slider_form = SliderForm(request.POST or None, instance=slider)
    if slider_form.is_valid():
        slider_type = slider_form.cleaned_data.get('type')
        form_type = type_base_forms.get(slider_type)

        if form_type is None:
            slider = slider_form.save()
        elif form_type.is_valid():
            slider = form_type.save()

        if form_type is None or form_type.is_valid():
            msg = pgettext_lazy('Slider message', 'Added slider')
            messages.success(request, msg)
            return redirect('dashboard:slider-details', pk)
    ctx = {
        'slider': slider,
        'form': slider_form,
        'type_base_forms': type_base_forms, }
    return TemplateResponse(
        request, 'dashboard/widget/slider/form.html', ctx)


@staff_member_required
@permission_required('widget.manage_sliders')
def slider_delete(request, pk):
    instance = get_object_or_404(Slider, pk=pk)
    if request.method == 'POST':
        instance.delete()
        msg = pgettext_lazy(
            'Slider message', 'Removed slider %s') % (instance,)
        messages.success(request, msg)
        return redirect('dashboard:slider-list')
    ctx = {'slider': instance}
    return TemplateResponse(
        request, 'dashboard/widget/slider/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def slide_create(request, slider_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    slide = Slide(slider_id=slider_pk)
    form = SlideForm(
        request.POST or None,
        request.FILES or None,
        instance=slide, )
    if form.is_valid():
        slide = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Nuevo slide añadido', ), )
        return redirect('dashboard:slider-details', pk=slider.pk)
    ctx = {
        'slider': slider,
        'slide': slide,
        'form': form, }
    return TemplateResponse(
        request,
        'dashboard/widget/slider/slide/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def slide_edit(request, slider_pk, slide_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    slide = get_object_or_404(Slide, pk=slide_pk)
    form = SlideForm(
        request.POST or None,
        request.FILES or None,
        instance=slide, )

    if form.is_valid():
        slide = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Slide actualizado', ), )
        return redirect('dashboard:slider-details', pk=slider.pk)

    ctx = {
        'slider': slider,
        'slide': slide,
        'form': form, }

    return TemplateResponse(
        request,
        'dashboard/widget/slider/slide/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def slide_delete(request, slider_pk, slide_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    slide = get_object_or_404(Slide, pk=slide_pk)
    if request.method == 'POST':
        slide.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Slider eliminado')
        messages.success(
            request,
            msg, )
        return redirect('dashboard:slider-details', pk=slider_pk)

    ctx = {
        'slider': slider,
        'slide': slide, }
    return TemplateResponse(
        request,
        'dashboard/widget/slider/slide/modal/confirm_delete.html',
        ctx)


@staff_member_required
@permission_required('site.manage_settings')
def ajax_reorder_slides(request, slider_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    form = ReorderSlideForm(
        request.POST or None,
        request.FILES or None,
        instance=slider,
    )
    status = 200
    ctx = {}
    if form.is_valid():
        form.save()
    elif form.errors:
        status = 400
        ctx = {'error': form.errors}
    return JsonResponse(ctx, status=status)
