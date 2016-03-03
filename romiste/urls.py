from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _

from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from romiste.models import ScientistPerson, RomanyThing

urlpatterns_romanyThing = repository_patterns(app_name='romiste_romanyThing', model=RomanyThing,
                                              search_facets=[],
                                              search_orderings=(
                                                  ('title', _('Sort by title')),
                                              ),
                                              search_default_ordering='title',
                                              add_parent_collection=lambda x: FedoraObject.objects.get(pk='romiste/recordings'),
                                              attachment_model=None, )

urlpatterns_scientistPerson = repository_patterns(app_name='romiste_scientistPerson', model=ScientistPerson,
                                                  search_facets=[],
                                                  search_orderings=(
                                                      ('surname', _('Sort by surname')),
                                                      ('-surname', _('Sort by surname (desc)')),
                                                  ),
                                                  search_default_ordering='surname',
                                                  add_parent_collection=lambda x: FedoraObject.objects.get(pk='romiste/scientists'),
                                                  attachment_model=None, )

urlpatterns = [
    url(r'recordings/', include(patterns('',
                                         *urlpatterns_romanyThing
                                         ))),
    url(r'scientists/', include(patterns('',
                                         *urlpatterns_scientistPerson
                                         )))
]
