"""oarepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from urlbreadcrumbs import url as burl
from django.utils.translation import ugettext_lazy as _
import baseOArepo.views

import dcterms.urls
from fedoralink_ui.generic_urls import repository_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    # url(r'^administration/', include("administration.urls")),
    # burl(r'^dcterms/', include("dcterms.urls"), verbose_name=_('DCterms')),
    # url(r'^romiste/', include("romiste.urls")),
    # # url(r'^states/', include("state_engi.ne.urls")),
    # url(r'^types/', include("types_engine.urls")),
    # # url(r'^types/', include("data_types.urls")),
    # url(r'^', include(patterns('',
    #                            url('^$', baseOArepo.views.index, name="index")), namespace='oarepo'))
]
urlpatterns += repository_patterns(app_name="oarepo")