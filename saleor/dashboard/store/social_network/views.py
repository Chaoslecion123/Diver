from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ....store.models import SocialNetwork
from ...views import staff_member_required
from .forms import SocialNetworkForm


@staff_member_required
@permission_required('site.manage_settings')
def social_network_add(request, site_settings_pk):
    social_network = SocialNetwork(site_settings_id=site_settings_pk)
    form = SocialNetworkForm(request.POST or None, instance=social_network)
    if form.is_valid():
        social_network = form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added social network %s') % (social_network,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'social_network': social_network}
    return TemplateResponse(
        request, 'dashboard/store/social_networks/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def social_network_edit(request, site_settings_pk, pk):
    social_network = get_object_or_404(SocialNetwork, pk=pk)
    form = SocialNetworkForm(request.POST or None, instance=social_network)
    if form.is_valid():
        social_network = form.save()
        msg = pgettext_lazy(
            'dashboard message', 'Updated social network %s') % (social_network,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk,
           'social_network': social_network}
    return TemplateResponse(
        request, 'dashboard/store/social_networks/form.html', ctx)


@staff_member_required
@permission_required('site.manage_settings')
def social_network_delete(request, site_settings_pk, pk):
    social_network = get_object_or_404(SocialNetwork, pk=pk)
    if request.method == 'POST':
        social_network.delete()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Removed site social network %s') %
            (social_network,))
        return redirect(
            'dashboard:site-details', pk=site_settings_pk)
    return TemplateResponse(
        request, 'dashboard/store/social_networks/modal/confirm_delete.html',
        {'social_network': social_network, 'site_settings_pk': site_settings_pk})
