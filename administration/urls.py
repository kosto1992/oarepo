from django.conf.urls import url, include, patterns

import administration.views

urlpatterns = [
    url(r'^', include(patterns('',
                               url('^$', administration.views.index, name="index")),
                      namespace='oarepo_administration', app_name='administration'))
]