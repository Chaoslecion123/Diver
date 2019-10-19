from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ....store.models import SpecialPage
from ...views import staff_member_required
from .forms import SpecialPageForm


@staff_member_required
@permission_required('site.manage_settings')
def special_page_add(request, site_settings_pk):
    special_page = SpecialPage(site_settings_id=site_settings_pk)
    form = SpecialPageForm(request.POST or None, instance=special_page)
    if form.is_valid():
        special_page = form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added special page %s') % (special_page,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'special_page': special_page}
    return TemplateResponse(
        request, 'dashboard/store/special_pages/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def special_page_edit(request, site_settings_pk, pk):
    special_page = get_object_or_404(SpecialPage, pk=pk)
    form = SpecialPageForm(request.POST or None, instance=special_page)
    if form.is_valid():
        special_page = form.save()
        msg = pgettext_lazy(
            'dashboard message', 'Updated special page %s') % (special_page,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'special_page': special_page}
    return TemplateResponse(
        request, 'dashboard/store/special_pages/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def special_page_delete(request, site_settings_pk, pk):
    special_page = get_object_or_404(SpecialPage, pk=pk)
    if request.method == 'POST':
        special_page.delete()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Removed site special page %s') %
            (special_page,))
        return redirect(
            'dashboard:site-details', pk=site_settings_pk)
    return TemplateResponse(
        request, 'dashboard/store/special_pages/modal/confirm_delete.html',
        {'special_page': special_page, 'site_settings_pk': site_settings_pk})
