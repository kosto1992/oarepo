import itertools

import django
from django.core.management import call_command
from django.db import connections

from fedoralink.indexer.models import IndexableFedoraObject
from fedoralink.models import FedoraObject
from fedoralink.type_manager import FedoraTypeManager

import logging
# logging.basicConfig(level=logging.INFO)

django.setup()


# at first setup elasticsearch data types for indexing
def fullname(o):
    return o.__module__ + "." + o.__name__

for model in FedoraTypeManager.models:
    if issubclass(model, IndexableFedoraObject):
        model_name = fullname(model)
        # if not model_name.startswith('fedoralink_ui'):
        print(model_name)
        call_command('config_repository_index_elasticsearch', model_name)


# now, reindex all documents in the repository ...
def iterate_all_documents(root):
    if isinstance(root, str):
        root = FedoraObject.objects.get(pk=root)

    if isinstance(root, IndexableFedoraObject):
        root.update()
        yield root
        for c in root.children:
            for it in iterate_all_documents(c):
                yield it

indexer = connections['repository'].indexer
# for doc in itertools.chain(#iterate_all_documents('theses'),
#                            iterate_all_documents('')):
#     indexer.reindex(doc)


