# -*- coding: utf-8 -*-
from django import template

from romiste.models import Video

register = template.Library()


@register.filter
def get_documents(id):
    print('get_documents')
    return Video.objects.get(pk=id)