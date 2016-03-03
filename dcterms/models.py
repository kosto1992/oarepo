from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import EBUCORE, FEDORA
from fedoralink.indexer.fields import IndexedTextField


class DocumentAttachment(DCObject):
    filename = IndexedTextField(EBUCORE.filename, verbose_name=_('File'))

    class Meta:
        rdf_types = (FEDORA.Binary, )
