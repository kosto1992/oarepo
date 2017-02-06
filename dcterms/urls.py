from django.conf import settings
from django.conf.urls import url, include
import fedoralink_ui.views
from urlbreadcrumbs import url as burl
from django.utils.translation import ugettext_lazy as _

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.models import FedoraObject

# TODO: zbavit sa model = DCObject, pridat template pre detail collection (search)
urlpatterns = [
    url('^$',
        fedoralink_ui.views.GenericDetailView.as_view(
            fedora_prefix='dcterms'), name="index"),
    burl(r'^(?P<collection_id>[a-fA-F0-9_/-]*)extended_search(?P<parameters>.*)$',
        fedoralink_ui.views.GenericSearchView.as_view(
            facets=(),
                                              orderings=(
                                ('title@en', _('Sort by title (asc)')),
                                ('-title@en', _('Sort by title (desc)')),
                        ),
                                              title='Documents',
                                              create_button_title='Create a New Document',
                                              fedora_prefix='dcterms'),
        name='extended_search', verbose_name=_('DCterms')),

    burl('^(?P<pk>.*)/addSubcollection$', fedoralink_ui.views.GenericSubcollectionCreateView.as_view(
        fedora_prefix='dcterms',
        success_url="dcterms:detail",
        parent_collection=lambda x: FedoraObject.objects.get(pk='dcterms'),
        success_url_param_names=('id',)
    ), name='addSubcollection'),

    burl('^(?P<pk>.*)/add$', fedoralink_ui.views.GenericCreateView.as_view(
                                                                              fedora_prefix='dcterms',
                                                                              success_url="dcterms:detail",
                                                                              parent_collection=lambda x: FedoraObject.objects.get(pk='dcterms'),
                                                                              success_url_param_names = ('id',)
                                                                           )
        , name='add'),

    burl('^(?P<id>.*)/edit$',
        fedoralink_ui.views.GenericEditView.as_view(
                 success_url="dcterms:detail",
            fedora_prefix='dcterms'
                 ),
        name="edit"),

    url('^(?P<id>.*)$',
        fedoralink_ui.views.GenericDetailView.as_view(
                                              fedora_prefix='dcterms'), name="detail"),
]

urlpatterns = [
    burl(r'^', include(urlpatterns, namespace='dcterms', app_name='dcterms'))
]

if settings.USE_BREADCRUMBS:
    import autobreadcrumbs.discover
    autobreadcrumbs.discover.autodiscover()