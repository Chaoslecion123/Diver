from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ....store.models import BankAccount
from ...views import staff_member_required
from .forms import BankAccountForm


@staff_member_required
@permission_required('site.manage_settings')
def bank_account_add(request, site_settings_pk):
    bank_account = BankAccount(site_settings_id=site_settings_pk)
    form = BankAccountForm(request.POST or None, instance=bank_account)
    if form.is_valid():
        bank_account = form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added bank account %s') % (bank_account,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'bank_account': bank_account}
    return TemplateResponse(
        request, 'dashboard/store/bank_account/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def bank_account_edit(request, site_settings_pk, pk):
    bank_account = get_object_or_404(BankAccount, pk=pk)
    form = BankAccountForm(request.POST or None, instance=bank_account)
    if form.is_valid():
        bank_account = form.save()
        msg = pgettext_lazy(
            'dashboard message', 'Updated bank account %s') % (bank_account,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'bank_account': bank_account}
    return TemplateResponse(
        request, 'dashboard/store/bank_account/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def bank_account_delete(request, site_settings_pk, pk):
    bank_account = get_object_or_404(BankAccount, pk=pk)
    if request.method == 'POST':
        bank_account.delete()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Removed site bank account %s') %
            (bank_account,))
        return redirect(
            'dashboard:site-details', pk=site_settings_pk)
    return TemplateResponse(
        request, 'dashboard/store/bank_account/modal/confirm_delete.html',
        {'bank_account': bank_account, 'site_settings_pk': site_settings_pk})
