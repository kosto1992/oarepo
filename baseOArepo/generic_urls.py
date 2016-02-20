from django.conf.urls import url, include, patterns


def repository_patterns(index, extended_search, add, detail, download, edit, namespace, custom_patterns = None):
    return [
    url(r'^', include(patterns('',
                               url(r'^$', index, name="index"),
                               #    breadcrumb=_('dcterms:index')),

                               url(r'^extended_search(?P<parametry>.*)$', extended_search,
                                  name='rozsirene_hledani'),
                               #    breadcrumb=_('Rozšířené hledání')),

                               url('^add$', add
                               , name='pridani_dcterms_object'),
                               #     breadcrumb=_('Přidání akreditace')),
                               #
                               url('^((?P<pk>[0-9a-z_-]+))$', detail, name="detail"),
                               # url('^((?P<id>[0-9a-z_-]+))$', dcterms.views.detail, name="detail"),
                               #     breadcrumb=_('dcterms:detail')),
                               #
                               url('^download/(?P<bitstream_id>[0-9a-z_-]+)$', download, name="download"),
                               #     breadcrumb=_('dcterms:download')),
                               url('^edit/((?P<pk>[0-9a-z_-]+))$', edit, name="detail"),

                               ),namespace=namespace))
]