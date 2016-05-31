from fedoralink.models import FedoraObject
from fedoralink_ui.models import DCTermsCollection, ResourceTypeCollection


def createCollection(name, model, slug):
    parent = FedoraObject.objects.get(pk='')
    typeObject = parent.create_child(name, flavour=model, slug=slug)
    typeObject.save()

#createCollection(name="type", model=ResourceTypeCollection, slug="type")
createCollection(name="dcterms", model=DCTermsCollection, slug="dcterms")