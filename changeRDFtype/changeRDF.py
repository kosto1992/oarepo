import django
from rdflib import URIRef
from rdflib.namespace import DC

from fedoralink.fedorans import RDF, CESNET
from fedoralink.models import FedoraObject
from oarepo import settings

django.setup()

import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def reindex(obj, level=0):
    if 'fedora:' in obj.id:
        return

    obj.update()
    types = obj[RDF.type]

    if not URIRef(DC.Object) in types:
        types.append(URIRef(DC.Object))
        obj[RDF.type] = types
        obj.save()

    print("   " * level, obj.id, type(obj))

    for c in obj.children:
        reindex(c, level + 1)

parent_collection = FedoraObject.objects.get(pk='theses')
reindex(parent_collection)

