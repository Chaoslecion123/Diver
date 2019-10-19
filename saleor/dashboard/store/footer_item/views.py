from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ....store.models import FooterItem
from ....site.models import SiteSettings
from ...views import staff_member_required
from .forms import FooterItemForm, ReorderFooterItemForm


@staff_member_required
@permission_required('site.manage_settings')
def footer_item_add(request, site_settings_pk):
    footer_item = FooterItem(site_settings_id=site_settings_pk)
    form = FooterItemForm(request.POST or None, instance=footer_item)
    if form.is_valid():
        footer_item = form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added bank account %s') % (footer_item,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'footer_item': footer_item}
    return TemplateResponse(
        request, 'dashboard/store/footer_item/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def footer_item_edit(request, site_settings_pk, pk):
    footer_item = get_object_or_404(FooterItem, pk=pk)
    form = FooterItemForm(request.POST or None, instance=footer_item)
    if form.is_valid():
        footer_item = form.save()
        msg = pgettext_lazy(
            'dashboard message', 'Updated bank account %s') % (footer_item,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'footer_item': footer_item}
    return TemplateResponse(
        request, 'dashboard/store/footer_item/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def footer_item_delete(request, site_settings_pk, pk):
    footer_item = get_object_or_404(FooterItem, pk=pk)
    if request.method == 'POST':
        footer_item.delete()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Removed site bank account %s') %
            (footer_item,))
        return redirect(
            'dashboard:site-details', pk=site_settings_pk)
    return TemplateResponse(
        request, 'dashboard/store/footer_item/modal/confirm_delete.html',
        {'footer_item': footer_item, 'site_settings_pk': site_settings_pk})


@staff_member_required
@permission_required('site.manage_settings')
def ajax_reorder_footer_items(request, site_settings_pk):
    site_settings = get_object_or_404(SiteSettings, pk=site_settings_pk)
    form = ReorderFooterItemForm(
        request.POST or None,
        request.FILES or None,
        instance=site_settings,
    )
    status = 200
    ctx = {}
    if form.is_valid():
        form.save()
    elif form.errors:
        status = 400
        ctx = {'error': form.errors}
    return JsonResponse(ctx, status=status)
