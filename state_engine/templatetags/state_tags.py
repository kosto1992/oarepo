import traceback

from django import template

from fedoralink.fedorans import CESNET_STATE
from state_engine.models import State, Transition

register = template.Library()


@register.filter
def fedora_states(obj):
    return [State.objects.get(pk=str(x)) for x in obj[CESNET_STATE.state]]


@register.filter
def fedora_transitions(state):
    # get all transitions from this state
    print(state)
    ret = []
    if state.allowed_state_transitions:
        for x in [state.allowed_state_transitions]:
            try:
                print("transition", x )
                ret.append(Transition.objects.get(pk=str(x)))
            except:
                traceback.print_exc()
    return ret