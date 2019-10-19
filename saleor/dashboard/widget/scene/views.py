from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import pgettext_lazy

from ....core.utils import get_paginator_items
from ....widget.models import Scene, Spotlight
from ...views import staff_member_required
from .filters import SceneFilter
from . import forms


@staff_member_required
@permission_required('site.manage_settings')
def scene_list(request):
    scenes = Scene.objects.all()
    scene_filter = SceneFilter(request.GET, queryset=scenes)
    scenes = get_paginator_items(
        scene_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'), )
    ctx = {
        'scenes': scenes,
        'filter_set': scene_filter,
        'is_empty': not scene_filter.queryset.exists()}
    return TemplateResponse(
        request,
        'dashboard/widget/scene/list.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def scene_details(request, pk):
    scene = get_object_or_404(Scene, pk=pk)
    ctx = {'scene': scene, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/detail.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def scene_create(request):
    scene = Scene()
    form = forms.SceneForm(
        request.POST or None,
        request.FILES or None,
        instance=scene, )
    if form.is_valid():
        scene = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message', 'Nuevo scene añadido'), )
        return redirect('dashboard:scene-list')
    ctx = {
        'scene': scene,
        'form': form, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def scene_edit(request, pk):
    scene = get_object_or_404(Scene, pk=pk)
    form = forms.SceneForm(
        request.POST or None,
        request.FILES or None,
        instance=scene, )
    if form.is_valid():
        scene = form.save()
        msg = pgettext_lazy('Dashboard message', 'Scene actualizado')
        messages.success(request, msg)
        return redirect('dashboard:scene-details', pk=pk)
    ctx = {
        'scene': scene,
        'form': form, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def scene_delete(request, pk):
    scene = get_object_or_404(Scene, pk=pk)
    if request.method == 'POST':
        scene.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Scene eliminado %s') % (scene.name,)
        messages.success(
            request,
            msg, )
        return redirect('dashboard:scene-list')
    ctx = {
        'scene': scene, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/modal/confirm_delete.html',
        ctx
    )


@staff_member_required
@permission_required('site.manage_settings')
def spotlight_create(request, scene_pk):
    scene = get_object_or_404(Scene, pk=scene_pk)
    spotlight = Spotlight(scene_id=scene_pk)
    form = forms.SpotlightForm(
        request.POST or None,
        request.FILES or None,
        instance=spotlight, )
    if form.is_valid():
        spotlight = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Nuevo spotlight añadido', ), )
        return redirect('dashboard:scene-details', pk=scene.pk)
    ctx = {
        'scene': scene,
        'spotlight': spotlight,
        'form': form, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/spotlight/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def spotlight_edit(request, scene_pk, spotlight_pk):
    scene = get_object_or_404(Scene, pk=scene_pk)
    spotlight = get_object_or_404(Spotlight, pk=spotlight_pk)
    form = forms.SpotlightForm(
        request.POST or None,
        request.FILES or None,
        instance=spotlight, )

    if form.is_valid():
        spotlight = form.save()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Spotlight actualizado', ), )
        return redirect('dashboard:scene-details', pk=scene.pk)

    ctx = {
        'scene': scene,
        'spotlight': spotlight,
        'form': form, }

    return TemplateResponse(
        request,
        'dashboard/widget/scene/spotlight/form.html',
        ctx, )


@staff_member_required
@permission_required('site.manage_settings')
def spotlight_delete(request, scene_pk, spotlight_pk):
    scene = get_object_or_404(Scene, pk=scene_pk)
    spotlight = get_object_or_404(Spotlight, pk=spotlight_pk)
    if request.method == 'POST':
        spotlight.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Scene eliminado')
        messages.success(
            request,
            msg, )
        return redirect('dashboard:scene-details', pk=scene_pk)

    ctx = {
        'scene': scene,
        'spotlight': spotlight, }
    return TemplateResponse(
        request,
        'dashboard/widget/scene/spotlight/modal/confirm_delete.html',
        ctx)
