from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class JWTConfig(AppConfig):
    name = 'saleor.jwt'
    label = 'jwt'
    verbose_name = _('JWT')
