from django.template import Library
from django.utils.encoding import iri_to_uri

register = Library()

def basic_media_prefix():
    """
    Returns the string contained in the setting BASIC_MEDIA_PREFIX.
    """
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return iri_to_uri(settings.BASIC_MEDIA_PREFIX)
basic_media_prefix = register.simple_tag(basic_media_prefix)
