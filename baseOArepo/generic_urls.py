import inspect

from django.core.urlresolvers import resolve

import fedoralink.views

from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _


def get_view(view_or_class, **kwargs):
    if inspect.isclass(view_or_class):
        return view_or_class.as_view(**kwargs)
    else:
        return view_or_class


def repository_patterns(app_name, model, index=fedoralink.views.GenericIndexView,
                        extended_search=fedoralink.views.GenericIndexerView,
                        add=fedoralink.views.GenericDocumentCreate, detail=fedoralink.views.GenericDetailView,
                        download=fedoralink.views.GenericDownloadView, edit=fedoralink.views.GenericEditView,
                        search_base_template='baseOArepo/search_base.html',
                        search_list_item_template='baseOArepo/repo_fragments/list/dokument.html',
                        search_facets=[
                            ('title', _('Dle nazvu')),
                        ],
                        search_orderings=(
                                ('title@cs', _('Dle nazvu')),
                                ('-title@cs', _('Dle nazvu')),
                        ),
                        search_default_ordering='title@cs',
                        add_template_name='baseOArepo/create.html',
                        add_parent_collection=None, add_success_url='index',
                        detail_template_name='baseOArepo/detail.html', detail_prefix="",
                        edit_template_name='baseOArepo/edit.html', edit_success_url='index', edit_prefix="",
                        attachment_model=None,
                        custom_patterns=None):
    pat = [
        url(r'^$', get_view(index, app_name=app_name), name="index"),
        #    breadcrumb=_('dcterms:index')),

        url(r'^extended_search(?P<parametry>.*)$',
            get_view(extended_search, model=model, base_template=search_base_template,
                     list_item_template=search_list_item_template, facets=search_facets,
                     orderings=search_orderings,
                     default_ordering=search_default_ordering),
            name='rozsirene_hledani'),
        #    breadcrumb=_('Rozšířené hledání')),

        url('^add$', get_view(add, model=model, template_name=add_template_name,
                             success_url=app_name + ":" + add_success_url,
                             parent_collection=add_parent_collection)
           , name='add'),
        #     breadcrumb=_('Přidání akreditace')),
        #
        url('^download/(?P<bitstream_id>[0-9a-z_-]+)$',
            get_view(download, model=attachment_model), name="download"),
        #     breadcrumb=_('dcterms:download')),
        url('^edit/(?P<pk>[^/]+)$',
            get_view(edit, model=model, template_name=edit_template_name,
                     success_url=app_name + ":" + edit_success_url, prefix=edit_prefix),
            name="edit"),
        url('^(?P<pk>[^/]+)$',
            get_view(detail, template_name=detail_template_name,
                     prefix=detail_prefix), name="detail"),
    ]

    if custom_patterns:
        pat.append(custom_patterns)

    return [
        url(r'^', include(patterns('',
                                   *pat
                                   ), namespace=app_name))
    ]

def appname(request):
    return {'appname': resolve(request.path).namespace}
