from django.conf.urls import url

import fedoralink
from baseOArepo.generic_urls import repository_patterns, get_view
from fedoralink.models import FedoraObject
from romiste.models import ScientistPerson, RomanyThing
from django.utils.translation import ugettext_lazy as _

urlpatterns = repository_patterns(app_name='romiste', model=RomanyThing,
                                  search_facets=[
                                      ('title', _('By title')),
                                  ],
                                  search_orderings=(
                                      ('title', _('By title')),
                                  ),
                                  search_default_ordering='title',
                                  add_parent_collection=lambda x: FedoraObject.objects.get(pk='test'),
                                  attachment_model=None, custom_patterns=url('^addPerson$', get_view(
        fedoralink.views.GenericDocumentCreate, model=ScientistPerson,
        template_name='baseOArepo/create.html',
        success_url="romiste:index",success_url_param_names=('pk',),
        parent_collection=None)
                                                                             , name='add'), )
