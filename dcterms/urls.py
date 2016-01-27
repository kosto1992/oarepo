from django.conf.urls import url, include, patterns
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DetailView, UpdateView
from fedoralink.models import FedoraObject
from fedoralink.common_namespaces.dc import DCObject

import dcterms.views
from fedoralink.views import GenericIndexerView


class DCTermsDokumentIndexerView(GenericIndexerView):
    model_class = 'fedoralink.common_namespaces.dc.DCObject'
    base_template = 'dcterms/search_base.html'
    list_item_template = 'dcterms/repo_fragments/list/dokument.html'
    facets = [
        ('title', _('Dle nazvu')),
    ]
    orderings = (
        ('title@cs', _('Dle nazvu')),
        ('-title@cs', _('Dle nazvu')),
    )
    default_ordering = 'title@cs'

class DCTermsDokumentCreate(CreateView):
    model = DCObject
    fields = '__all__'
    template_name = 'dcterms/create.html'
    parent_collection = None

    def get_success_url(self):
        created = self.object
        return reverse('dcterms:index')

    def form_valid(self, form):
        inst = form.save(commit=False)
        inst.save()
        self.object = inst

        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        ret = super().get_form_kwargs()

        if callable(self.parent_collection):
            parent = self.parent_collection(self)
        else:
            parent = self.parent_collection

        self.object = ret['instance'] = parent.create_child('', flavour=self.model)

        return ret

class DCTermsEditView(UpdateView):
    model = DCObject
    fields = '__all__'
    template_name = 'dcterms/edit.html'

    prefix = None

    def get_success_url(self):
        created = self.object
        return reverse('dcterms:index')

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, queryset=None):
        pk = self.prefix + self.kwargs.get(self.pk_url_kwarg, None).replace("_","/")
        self.kwargs[self.pk_url_kwarg]=pk
        print(self.kwargs)
        return super().get_object(queryset)



class DCTermsDetailView(DetailView):
    model = DCObject
    prefix = None
    template_name = "dcterms/detail.html"

    # DCObject.all_indexed_fields()
    # DCObject.

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, queryset=None):
        pk = self.prefix + self.kwargs.get(self.pk_url_kwarg, None).replace("_","/")
        self.kwargs[self.pk_url_kwarg]=pk
        print(self.kwargs)
        return super().get_object(queryset)

    model = DCObject

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