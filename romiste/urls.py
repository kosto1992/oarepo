from django.conf.urls import url, include, patterns

import fedoralink
from baseOArepo.generic_urls import repository_patterns, get_view
from fedoralink.models import FedoraObject
from romiste.models import ScientistPerson, RomanyThing
from django.utils.translation import ugettext_lazy as _

urlpatterns_romanyThing = repository_patterns(app_name='romiste_romanyThing', model=RomanyThing,
                                              search_facets=[
                                                  ('title', _('By title')),
                                              ],
                                              search_orderings=(
                                                  ('title', _('By title')),
                                              ),
                                              search_default_ordering='title',
                                              add_parent_collection=lambda x: FedoraObject.objects.get(pk='test'),
                                              attachment_model=None, )
urlpatterns_scientistPerson = repository_patterns(app_name='romiste_scientistPerson', model=ScientistPerson,
                                                  search_facets=[
                                                      ('surname', _('By surame')),
                                                  ],
                                                  search_orderings=(
                                                      ('surname', _('By surname')),
                                                  ),
                                                  search_default_ordering='surname',
                                                  add_parent_collection=lambda x: FedoraObject.objects.get(pk='test'),
                                                  attachment_model=None, )

urlpatterns = [
    url(r'recordings/', include(patterns('',
                                         *urlpatterns_romanyThing
                                         ))),
    url(r'scientists/', include(patterns('',
                                         *urlpatterns_scientistPerson
                                         )))
]
