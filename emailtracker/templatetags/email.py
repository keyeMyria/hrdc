from django import template
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()

@register.inclusion_tag("emailtracker/image.html", takes_context=True)
def image(context, fn, alt="Image", **kwargs):
    if context.get("IS_HTML", True):
        # Force hotlinking images
        cid = None # context["MESSAGE"].attach_inline_image_file(fn)
    else:
        return { "noimage": True }
    attrs = mark_safe(" ".join([format_html('{}="{}"', i, j) for i, j
                                in kwargs.items()]))
    if cid:
        return { "src": "cid:" + cid, "alt": alt, "attrs": attrs }
    else:
        return { "alt": alt, "src": settings.SITE_URL + 
                 static(fn.rpartition("/static/")[-1]),
                 "attrs": attrs }

@register.inclusion_tag("emailtracker/href.html", takes_context=True)
def href(context, url, text, *args, **kwargs):
    url = reverse(url, args=args)
    args = " ".join(['{}={}'.format(i, j) for i, j in kwargs.items()])
    return { "url": settings.SITE_URL + url,
             "text": text,
             "is_html": context.get("IS_HTML", True),
             "args": args }
