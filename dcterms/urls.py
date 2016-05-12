from django.conf.urls import url, include, patterns

import fedoralink_ui.views
from django.utils.translation import ugettext_lazy as _

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.models import FedoraObject

# TODO: zbavit sa model = DCObject, pridat template pre detail collection (search)
urlpatterns = [
    url(r'^$', fedoralink_ui.views.GenericIndexView.as_view(app_name='dcterms'), name="index"),
    #    breadcrumb=_('dcterms:index')),

    url(r'^extended_search(?P<parameters>.*)$',
        fedoralink_ui.views.GenericSearchView.as_view(model = DCObject,
            facets=(),
                                              orderings=(
                                ('title@en', _('Sort by title (asc)')),
                                ('-title@en', _('Sort by title (desc)')),
                        ),
                                              default_ordering='title@en',
                                              title='Documents',
                                              create_button_title='Create a New Document'),
        name='extended_search'),
    #    breadcrumb=_('Rozšířené hledání')),

    # url(r'^link-title/(?P<pk>[^/]+)$',
    #     get_view(link_title, model=model, template_name=link_title_template, prefix=detail_prefix),
    #     name='link_title'),
    #    breadcrumb=_('Rozšířené hledání')),

    # url(r'^link(?P<parametry>.*)$',
    #     get_view(link, model=model, base_template=link_base_template,
    #              list_item_template=link_list_item_template, facets=search_facets,
    #              orderings=search_orderings,
    #              default_ordering=search_default_ordering,
    #              title=labels.get('search_title', 'Documents')),
    #     name='link'),
    #    breadcrumb=_('Rozšířené hledání')),

    url('^add/(?P<pk>[^/]+)*$', fedoralink_ui.views.GenericCreateView.as_view(model=DCObject,
                                                                              success_url="dcterms:detail",
                                                                              parent_collection=lambda x: FedoraObject.objects.get(pk='dcterms'),
                                                                              success_url_param_names = ('pk',))
        , name='add'),
    #     breadcrumb=_('Přidání akreditace')),
    #
    # url('^download/(?P<bitstream_id>[0-9a-z_-]+)$',
    #     get_view(download, model=attachment_model), name="download"),
    #     breadcrumb=_('dcterms:download')),
    url('^edit/(?P<pk>[^/]+)$',
        fedoralink_ui.views.GenericEditView.as_view(model=DCObject,
                 success_url="dcterms:detail",
                 success_url_param_names=('pk',)
                 ),
        name="edit"),
    #
    # url('^change_state/(?P<pk>[^/]+)$',
    #     get_view(change_state), name="change_state"),

    url('^(?P<pk>[^/]+)$',
        fedoralink_ui.views.GenericDetailView.as_view(), name="detail"),

    url('^collection_detail(?P<parameters>.*)$',
        fedoralink_ui.views.GenericCollectionDetailView.as_view(), name="collectionDetail"),
]

urlpatterns = [
    url(r'^', include(patterns('',
                               *urlpatterns
                               ), namespace='dcterms', app_name='dcterms'))
]