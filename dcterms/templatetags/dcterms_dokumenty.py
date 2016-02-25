# -*- coding: utf-8 -*-
import inspect
import traceback
from urllib.parse import quote

from django import template
import logging

import django.utils.translation
from django.contrib.contenttypes.models import ContentType
from django.template import Context
from django.template.loader import select_template

from dcterms.models import DocumentAttachment
from django.conf import settings

register = template.Library()


@register.filter
def get_document(id):
    return DocumentAttachment.objects.get(pk=id)
