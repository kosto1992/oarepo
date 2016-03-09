from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.common_namespaces.web_acl.models import Authorization
from fedoralink.fedorans import CESNET_STATE, ACL, RDFS
from fedoralink.indexer.fields import IndexedLinkedField, IndexedTextField, IndexedField
from fedoralink.indexer.models import IndexableFedoraObject


class StateCollection(IndexableFedoraObject):

    class Meta:
        rdf_types = (CESNET_STATE.StateCollection, )


class State(IndexableFedoraObject):

    label = IndexedTextField(CESNET_STATE.label, verbose_name=_('Label'), level=IndexedField.MANDATORY)

    initial = IndexedTextField(CESNET_STATE.initial, verbose_name=_('Initial state'), level=IndexedField.MANDATORY,
                               choices=(('false', 'false'), ('true', 'true')))

    comment = IndexedTextField(CESNET_STATE.comment, verbose_name=_('Comment'), attrs={'presentation': 'textarea'})

    default_access_control = IndexedLinkedField(CESNET_STATE.defaultAccessControl, Authorization,
                                                verbose_name=_('Default Access Control Authorization'),
                                                multi_valued=False, level=IndexedField.RECOMMENDED)

    allowed_state_transitions = IndexedLinkedField(CESNET_STATE.allowedStateTransitions, 'state_engine.Transition',
                                                   verbose_name=_('Allowed Transitions From This State'),
                                                   multi_valued=False, level=IndexedField.RECOMMENDED)

    prohibited_state_transitions = IndexedLinkedField(CESNET_STATE.prohibitedStateTransitions, 'state_engine.Transition',
                                                      verbose_name=_('Prohibited Transitions From This State'),
                                                      multi_valued=False, level=IndexedField.RECOMMENDED)

    class Meta:
        rdf_types = (CESNET_STATE.State, )


class Transition(IndexableFedoraObject):

    label = IndexedTextField(CESNET_STATE.label, verbose_name=_('Label'), level=IndexedField.MANDATORY)

    comment = IndexedTextField(CESNET_STATE.comment, verbose_name=_('Comment'), attrs={'presentation': 'textarea'})

    target_state = IndexedLinkedField(CESNET_STATE.targetState, State, verbose_name=_('Transition target state'),
                                      level=IndexedField.RECOMMENDED)

    agent        = IndexedTextField(ACL.agent, verbose_name=_('People allowed to make the transition'),
                                    multi_valued=True, level=IndexedField.RECOMMENDED)

    agent_class  = IndexedTextField(ACL.agentClass, verbose_name=_('Groups allowed to make the transition'),
                                    multi_valued=True, level=IndexedField.RECOMMENDED)

    class Meta:
        rdf_types = (CESNET_STATE.Transition, )

