from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from fedoralink.fedorans import CESNET_STATE
from fedoralink.models import FedoraObject
from fedoralink.type_manager import FedoraTypeManager
from fedoralink.views import ModelViewRegistry
from state_engine.models import Transition


def index(req):
    return render(req, 'state_engine/index.html')

def index_romiste(req):
    return render(req, 'state_engine/index_romiste.html')



class GenericChangeStateView(View):
    model = None

    def post(self, request, pk):
        current_object = FedoraObject.objects.get(pk=pk.replace('_', '/'))
        state_pk = request.POST['state']
        transition = Transition.objects.get(pk=request.POST['transition'])
        target_state = transition.target_state
        states = current_object[CESNET_STATE.state]
        for statei, state in enumerate(states):
            if str(state) == str(state_pk):
                states = states[:statei] + states[statei+1:]
                break
        states.append(target_state)
        current_object[CESNET_STATE.state] = states
        current_object.save()
        return HttpResponseRedirect(reverse(ModelViewRegistry.get_view(type(current_object), 'detail'), kwargs={'pk':pk}))
