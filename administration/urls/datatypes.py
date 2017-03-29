from django.conf.urls import url, include

import administration.views.datatypes

urlpatterns = [
   url('^$', administration.views.datatypes.IndexView.as_view(), name="index"),
]
