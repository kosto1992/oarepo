from django.db import models

from django.utils.translation import ugettext_lazy as _
from rdflib.namespace import DC

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import CESNET
from fedoralink.indexer.fields import IndexedLanguageField, IndexedTextField, IndexedDateTimeField, IndexedBinaryField
from fedoralink.indexer.models import IndexableFedoraObject


class AttachmentsCollection (DCObject):

    class Meta:
        rdf_types = (CESNET.AttachmentsCollection,)

class Attachment (IndexableFedoraObject):

    class Meta:
        rdf_types = (CESNET.Attachment,)

class DCObjectWithAttachment(DCObject):

    attachment        = IndexedBinaryField(CESNET.attachment, Attachment,
                                       verbose_name=_('Attachment'))

    class Meta:
        rdf_types = (CESNET.DCObjectWithAttachment,)

