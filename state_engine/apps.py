from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rdflib import URIRef

from fedoralink.fedorans import CESNET_STATE
from fedoralink.models import FedoraObject


class ApplicationConfig(AppConfig):
    name = 'state_engine'
    verbose_name = _("state_engine")

    def ready(self):
        super().ready()


@receiver(pre_save)
def state_callback(sender, instance, *args, **kwargs):
    if not hasattr(sender,"_meta"):
        return
    if not hasattr(sender._meta, 'state_collection'):
        return

    state_collections = sender._meta.state_collection
    print("Objects is handled by state collection", state_collections)

    state_control = instance[CESNET_STATE.stateControl]
    if not state_control:

        states = []
        state_collection_uris = []

        # TODO: this should be moved directly to the server
        for state_control in state_collections:
            state_collection_object = FedoraObject.objects.get(pk=str(state_control))
            state_collection_uris.append(state_collection_object.id)
            for state in state_collection_object.children:
                if state.initial.value == 'true':
                    states.append(state.id)
                    break
            else:
                raise AttributeError("There is no initial state in state collection %s" % state_collection_object.id)

        instance[CESNET_STATE.state] = states
        instance[CESNET_STATE.stateControl] = state_collection_uris
