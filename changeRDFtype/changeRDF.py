import django
from rdflib import URIRef
from rdflib.namespace import DC

from fedoralink.fedorans import RDF, CESNET
from fedoralink.models import FedoraObject
from oarepo import settings

django.setup()

parent_collection = FedoraObject.objects.get(pk='test')
parent = parent_collection
children = parent.list_children()
print(children)
for child in children:
    types = child[RDF.type]
    if (URIRef(CESNET.RomanyThing) in types) or (URIRef(CESNET.ScientistPerson) in types):
        continue
    types.append(URIRef(RDF.Object))
    child[RDF.type] = types
    print(child[DC.title])
    child.save()
