from django.conf.urls import url, include, patterns
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
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

urlpatterns = [
    url(r'^', include(patterns('',
                               url(r'^$', dcterms.views.index, name="index"),
                               #    breadcrumb=_('dcterms:index')),

                               url(r'^extended_search(?P<parametry>.*)$', DCTermsDokumentIndexerView.as_view(),
                                  name='rozsirene_hledani'),
                               #    breadcrumb=_('Rozšířené hledání')),

                               url('^add$', DCTermsDokumentCreate.as_view(
                                   parent_collection=lambda x: FedoraObject.objects.get(pk='test')
                               ), name='pridani_dcterms_object'),
                               #     breadcrumb=_('Přidání akreditace')),
                               #
                               url('^((?P<pk>[0-9a-z_-]+))$', DCTermsDetailView.as_view(prefix = "test/"), name="detail"),
                               # url('^((?P<id>[0-9a-z_-]+))$', dcterms.views.detail, name="detail"),
                               #     breadcrumb=_('dcterms:detail')),
                               #
                               url('^download/(?P<bitstream_id>[0-9a-z_-]+)$', dcterms.views.download, name="download"),
                               #     breadcrumb=_('dcterms:download')),
                               url('^edit/((?P<pk>[0-9a-z_-]+))$', DCTermsEditView.as_view(prefix = "test/"), name="detail"),

                               ),namespace="dcterms"))
]