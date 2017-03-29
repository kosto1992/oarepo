from django.conf.urls import include, url

from .datatypes import urlpatterns as datatypes_urlpatterns
from .index import urlpatterns as index_urlpatterns

base_urlpatterns = [
    url(r'^datatypes/', include(datatypes_urlpatterns,
                                namespace='oarepo_administration_datatypes', app_name='administration')),
    url(r'^', include(index_urlpatterns, namespace='oarepo_administration', app_name='administration'))
]

urlpatterns = [
    url(r'^', include(base_urlpatterns)),
]
