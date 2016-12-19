from baseOArepo.models import AttachmentsCollection
from fedoralink.authentication.Credentials import Credentials
from fedoralink.authentication.as_user import as_user
from fedoralink.models import FedoraObject
from fedoralink_ui.models import DCTermsCollection, ResourceTypeCollection, AdministrationCollection


def createCollection(name, model, slug, pk=""):
    parent = FedoraObject.objects.get(pk=pk)
    typeObject = parent.create_child(name, flavour=model, slug=slug)
    typeObject.save()

import configparser
config = configparser.ConfigParser()
config.read('../oarepo/admin_auth.cfg')

credentials = Credentials(config['oarepo']['admin'],config['oarepo']['admin_pw'])
print("user:" + credentials.username)
with as_user(credentials):
    # createCollection(name="administration", model=AdministrationCollection, slug="administration")
    # createCollection(name="types", model=ResourceTypeCollection, slug="types", pk='administration')
    # createCollection(name="dcterms", model=DCTermsCollection, slug="dcterms")
    createCollection(name="dcobjects with attachments", model=AttachmentsCollection, slug="attachments")