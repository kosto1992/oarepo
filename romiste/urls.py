from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _

from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from romiste.models import ScientistPerson, RomanyThing, Place, RomanyPerson
import romiste.view

urlpatterns_romanyThing = repository_patterns(app_name='romiste_romanyThing', model=RomanyThing,
                                              search_facets=[],
                                              search_orderings=(
                                                  ('title', _('Sort by title')),
                                              ),
                                              search_default_ordering='title',
                                              search_list_item_template='romiste/repo_fragments/list/recordings.html',
                                              detail_template_name='romiste/recordings/detail.html',
                                              add_parent_collection=lambda x: FedoraObject.objects.get(
                                                  pk='romiste/recordings'),
                                              attachment_model=None, )

urlpatterns_scientistPerson = repository_patterns(app_name='romiste_scientistPerson', model=ScientistPerson,
                                                  search_facets=[],
                                                  search_orderings=(
                                                      ('surname', _('Sort by surname')),
                                                      ('-surname', _('Sort by surname (desc)')),
                                                  ),
                                                  search_list_item_template='romiste/repo_fragments/list/person.html',
                                                  detail_template_name='romiste/scientists/detail.html',
                                                  search_default_ordering='surname',
                                                  add_parent_collection=lambda x: FedoraObject.objects.get(
                                                      pk='romiste/scientists'),
                                                  attachment_model=None, )
urlpatterns_romanyPerson = repository_patterns(app_name='romiste_romanyPerson', model=RomanyPerson,
                                               search_facets=[],
                                               search_orderings=(
                                                   ('surname', _('Sort by surname')),
                                                   ('-surname', _('Sort by surname (desc)')),
                                               ),
                                               search_list_item_template='romiste/repo_fragments/list/person.html',
                                               detail_template_name='romiste/scientists/detail.html',
                                               search_default_ordering='surname',
                                               add_parent_collection=lambda x: FedoraObject.objects.get(
                                                   pk='romiste/respondents'),
                                               attachment_model=None,
                                               labels={
                                            'search_title': _('Respondents'),
                                            'create_title': _('Add a New Respondent'),
                                            'create_button_title': _('Add a Respondent')
                                        },)

urlpatterns_place = repository_patterns(app_name='romiste_place', model=Place,
                                        search_facets=[],
                                        search_orderings=(
                                            ('title', _('Sort by name')),
                                        ),
                                        search_default_ordering='title',
                                        add_parent_collection=lambda x: FedoraObject.objects.get(pk='romiste/places'),
                                        search_list_item_template='romiste/repo_fragments/list/place.html',
                                        attachment_model=None,
                                        labels={
                                            'search_title': _('Places'),
                                            'create_title': _('Add a New Place'),
                                            'create_button_title': _('Add a New Place'),
                                            'edit_title': _('Edit Place')
                                        },
                                        )

urlpatterns = [
    url(r'recordings/', include(patterns('',
                                         *urlpatterns_romanyThing
                                         ))),
    url(r'scientists/', include(patterns('',
                                         *urlpatterns_scientistPerson
                                         ))),
    url(r'places/', include(patterns('',
                                     *urlpatterns_place
                                     ))),
    url(r'respondents/', include(patterns('',
                                         *urlpatterns_romanyPerson
                                         ))),
    url(r'^', include(patterns('',
                               url('^$', romiste.view.index, name="index")), namespace='romiste'))
]
