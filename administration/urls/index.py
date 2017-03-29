from django.conf.urls import url, include

import administration.views.index

urlpatterns = [
   url('^$', administration.views.index.IndexView.as_view(), name="index"),
]
