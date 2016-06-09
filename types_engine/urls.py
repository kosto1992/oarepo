from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _

import types_engine.views

urlpatterns = [
    url(r'', include(patterns('',
                              url(r'^$', types_engine.views.index, name='index'),
                              ), namespace='types_engine', app_name='types_engine')),
]
