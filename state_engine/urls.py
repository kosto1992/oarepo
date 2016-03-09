from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _

import state_engine.views
from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from state_engine.models import State, Transition

urlpatterns_state = repository_patterns(app_name='state_engine_states', model=State,
                                        search_list_item_template='state_engine/fragments/search_state.html',
                                        link_list_item_template='state_engine/fragments/link_state.html',
                                        add_parent_collection=lambda x: FedoraObject.objects.get(pk='states/states'),
                                        search_orderings=(
                                            ('label', _('Sort by label (asc)')),
                                            ('-label', _('Sort by label (desc)')),
                                        ),
                                        search_default_ordering='label',
                                        labels={
                                            'search_title': _('States'),
                                            'create_title': _('Adding New State'),
                                            'create_button_title': _('Add a New State')
                                        })

urlpatterns_transition = repository_patterns(app_name='state_engine_transitions', model=Transition,
                                             search_list_item_template='state_engine/fragments/search_transition.html',
                                             link_list_item_template='state_engine/fragments/search_transition.html',
                                             add_parent_collection=lambda x: FedoraObject.objects.get(
                                                     pk='states/transitions'),
                                             search_orderings=(
                                                 ('label', _('Sort by label (asc)')),
                                                 ('-label', _('Sort by label (desc)')),
                                             ),
                                             search_default_ordering='label',
                                             labels={
                                                 'search_title': _('Transitions'),
                                                 'create_title': _('Adding New Transition'),
                                                 'create_button_title': _('Add a New Transition')
                                             })

urlpatterns = [
    url(r'states/', include(patterns('',
                                     *urlpatterns_state
                                     ))),
    url(r'transitions/', include(patterns('',
                                          *urlpatterns_transition
                                          ))),
    url(r'', include(patterns('',
                              url(r'^romiste$', state_engine.views.index_romiste, name='index_romiste'),
                              url(r'^$', state_engine.views.index, name='index'),
                              ), namespace='state_engine')),
]
