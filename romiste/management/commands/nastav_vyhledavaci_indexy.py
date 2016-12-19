import django
import requests
from django.conf import settings
from django.core.management import call_command
from django.db import connections

from fedoralink.authentication.Credentials import Credentials
from fedoralink.authentication.as_user import as_user
from fedoralink.indexer.models import IndexableFedoraObject
from fedoralink.models import FedoraObject
from fedoralink.type_manager import FedoraTypeManager

# logging.basicConfig(level=logging.INFO)

django.setup()


# at first setup elasticsearch data types for indexing
def fullname(o):
    return o.__module__ + "." + o.__name__


# 1. remove everything from index

import configparser
config = configparser.ConfigParser()
config.read('../oarepo/admin_auth.cfg')

credentials = Credentials(config['oarepo']['admin'],config['oarepo']['admin_pw'])
print("user:" + credentials.username)
with as_user(credentials):
    requests.delete(settings.DATABASES['repository']['SEARCH_URL'])

    # 2. install schemas
    for model in FedoraTypeManager.models:
        if issubclass(model, IndexableFedoraObject):
            model_name = fullname(model)
            call_command('config_repository_index_elasticsearch', model_name)


# 3. reindex all documents in the repository ...
def iterate_all_documents(root):
    if isinstance(root, str):
        root = FedoraObject.objects.get(pk=root)

    root.update()
    if isinstance(root, IndexableFedoraObject):
        yield root

    for c in root.children:
        for it in iterate_all_documents(c):
            yield it

with as_user(credentials):
    indexer = connections['repository'].indexer
    for doc in iterate_all_documents(''):
        indexer.reindex(doc)


