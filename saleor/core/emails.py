from django.contrib.sites.models import Site
from django.templatetags.static import static
from django.urls import reverse_lazy
from ..core.utils import build_absolute_uri


def get_email_base_context():
    site = Site.objects.get_current()
    logo_url = build_absolute_uri(static('images/logo-light.svg'))
    login_url = build_absolute_uri(str(reverse_lazy('frontend:auth-login')))
    home_url = build_absolute_uri(str(reverse_lazy('frontend:storefront-home')))

    return {
        'domain': site.domain,
        'logo_url': logo_url,
        'login_url': login_url,
        'home_url': home_url,
        'site_name': site.name
    }
