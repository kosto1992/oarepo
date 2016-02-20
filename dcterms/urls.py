from django.conf.urls import url, include, patterns
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from fedoralink.common_namespaces.dc import DCObject

import dcterms.views
from fedoralink.views import GenericIndexerView, GenericDocumentCreate, GenericDetailView, GenericEditView

class DCTermsDokumentIndexerView(GenericIndexerView):
    model = DCObject
    base_template = 'baseOArepo/search_base.html'
    list_item_template = 'baseOArepo/repo_fragments/list/dokument.html'
    facets = [
        ('title', _('Dle nazvu')),
    ]
    orderings = (
        ('title@cs', _('Dle nazvu')),
        ('-title@cs', _('Dle nazvu')),
    )
    default_ordering = 'title@cs'

class DCTermsDokumentCreate(GenericDocumentCreate):
    model = DCObject
    template_name = 'baseOArepo/create.html'

    def get_success_url(self):
        created = self.object
        return reverse('dcterms:index')

class DCTermsEditView(GenericEditView):
    model = DCObject
    fields = '__all__'
    template_name = 'baseOArepo/edit.html'

    prefix = None

    def get_success_url(self):
        created = self.object
        return reverse('dcterms:index')

class DCTermsDetailView(GenericDetailView):
    model = DCObject
    prefix = None
    template_name = "baseOArepo/detail.html"

urlpatterns = repository_patterns(index=dcterms.views.index, extended_search=DCTermsDokumentIndexerView.as_view(), add=DCTermsDokumentCreate.as_view(
                                   parent_collection=lambda x: FedoraObject.objects.get(pk='test')
                               ), detail=DCTermsDetailView.as_view(prefix = "test/"), download=dcterms.views.download, edit=DCTermsEditView.as_view(prefix = "test/"), namespace="dcterms")
