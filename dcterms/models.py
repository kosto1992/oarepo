from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import EBUCORE, FEDORA
from fedoralink.indexer import BINARY, IndexedField
from fedoralink.type_manager import FedoraTypeManager


class DocumentAttachment(DCObject):
    indexed_fields = [
        IndexedField('filename', EBUCORE.filename, stored=True, indexed=True,
                     type=BINARY, prefix='ebucore_filename_',
                     verbose_name=_('Soubor')),
    ]

    def created(self):
        super().created()
        self.types.add(DCObject)

FedoraTypeManager.register_model(DocumentAttachment, on_rdf_type=[FEDORA.Binary])