from django.conf.urls import url, include, patterns
from django.utils.translation import ugettext_lazy as _

from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from fedoralink_ui.models import ResourceType

urlpatterns_type = repository_patterns(app_name='data_types', model=ResourceType,
                                       search_list_item_template='data_types/fragments/search_type.html',
                                       link_list_item_template='data_types/fragments/link_type.html',
                                       add_parent_collection=lambda x: FedoraObject.objects.get(pk='type'),
                                       search_orderings=(
                                            ('label', _('Sort by label (asc)')),
                                            ('-label', _('Sort by label (desc)')),
                                        ),
                                       search_default_ordering='label',
                                       labels={
                                            'search_title': _('Types'),
                                            'create_title': _('Add New Type'),
                                            'create_button_title': _('Add a New Type')
                                        })

# urlpatterns_transition = repository_patterns(app_name='state_engine_transitions', model=Transition,
#                                              search_list_item_template='state_engine/fragments/search_transition.html',
#                                              link_list_item_template='state_engine/fragments/search_transition.html',
#                                              add_parent_collection=lambda x: FedoraObject.objects.get(
#                                                      pk='states/transitions'),
#                                              search_orderings=(
#                                                  ('label', _('Sort by label (asc)')),
#                                                  ('-label', _('Sort by label (desc)')),
#                                              ),
#                                              search_default_ordering='label',
#                                              labels={
#                                                  'search_title': _('Transitions'),
#                                                  'create_title': _('Adding New Transition'),
#                                                  'create_button_title': _('Add a New Transition')
#                                              })

urlpatterns = [
    url(r'', include(patterns('',
                                     *urlpatterns_type
                                     ))),
    # url(r'transitions/', include(patterns('',
    #                                       *urlpatterns_transition
    #                                       ))),
]
