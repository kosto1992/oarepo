from fedoralink.models import FedoraObject
from fedoralink_ui.models import DCTermsCollection, ResourceTypeCollection, AdministrationCollection


def createCollection(name, model, slug, pk=""):
    parent = FedoraObject.objects.get(pk=pk)
    typeObject = parent.create_child(name, flavour=model, slug=slug)
    typeObject.save()

createCollection(name="administration", model=AdministrationCollection, slug="administration")
createCollection(name="types", model=ResourceTypeCollection, slug="types", pk='administration')
createCollection(name="dcterms", model=DCTermsCollection, slug="dcterms")