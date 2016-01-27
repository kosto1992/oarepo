# -*- coding: utf-8 -*-
import traceback
from urllib.parse import quote

from django import template
import logging

import django.utils.translation

from dcterms.models import DocumentAttachment

register = template.Library()


@register.filter
def rdf2lang(rdfliteral, lang=None):
    default_value = ''
    try:
        if lang is None:
            lang = django.utils.translation.get_language()
        if lang:
            lang = lang.split("-")[0]
        for l in rdfliteral:
            if lang and l.language == lang or (not lang and (l.language is None or l.language == '')):
                return l.value
            elif not l.language:
                default_value = l.value
    except:
        pass
    return default_value


@register.filter
def id_from_path(idval):
    return quote(idval[idval.find('test') + 1 + len('test'):]).replace('/', '_')


@register.filter
def get_document(id):
    return DocumentAttachment.objects.get(pk=id)


@register.filter
def get_fields(object):
    meta_fields = object._meta.fields
    fields=()
    for meta in meta_fields:
        meta_name = getattr(meta, "name")
        name = getattr(meta, "verbose_name")
        if name is None:
            name = meta_name
        fields += ((name, getattr(object, meta_name)),)

    return fields

