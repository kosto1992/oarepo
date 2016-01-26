# -*- coding: utf-8 -*-
import traceback
from urllib.parse import quote

from django import template
import logging

import django.utils.translation

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
            print(l.value)
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
