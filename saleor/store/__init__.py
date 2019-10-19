from django.utils.translation import pgettext_lazy


class SocialNetworkProvider:
    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'
    YOUTUBE = 'youtube'
    TWITTER = 'twitter'
    PINTEREST = 'pinterest'

    CHOICES = (
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'Youtube'),
        (TWITTER, 'Twitter'),
        (PINTEREST, 'Pinterest'), )


class PageType:
    ABOUT = 'about'
    FAQ = 'faq'
    LEGAL = 'legal'
    PRIVACY = 'privacy'
    ACCESSIBILITY = 'accessibility'

    CHOICES = (
        (ABOUT, pgettext_lazy(
            'Special page type', 'About')),
        (FAQ, pgettext_lazy(
            'Special page type', 'FAQ')),
        (LEGAL, pgettext_lazy(
            'Special page type', 'Terms and Conditions')),
        (PRIVACY, pgettext_lazy(
            'Special page type', 'Privacy and Cookies')),
        (ACCESSIBILITY, pgettext_lazy(
            'Special page type', 'Accessibility')), )


class BankProvider:
    BBVA = 'bbva'
    BCP = 'bcp'
    INTERBANK = 'interbank'

    CHOICES = (
        (BBVA, pgettext_lazy(
            'Bank name', 'BBVA Banco continental')),
        (BCP, pgettext_lazy(
            'Bank name', 'Banco de Crédito del Perú')),
        (INTERBANK, pgettext_lazy(
            'Bank name', 'Interbank')),
    )

    LONGNAMES = dict(CHOICES)

    SHORTNAMES = {
        BBVA: 'BBVA',
        BCP: 'BCP',
        INTERBANK: 'Interbank',
    }
