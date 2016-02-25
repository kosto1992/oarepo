from baseOArepo.generic_urls import repository_patterns
from dcterms.models import DocumentAttachment
from fedoralink.models import FedoraObject
from fedoralink.common_namespaces.dc import DCObject

urlpatterns = repository_patterns(app_name = 'dcterms', model=DCObject,
                                  add_parent_collection=lambda x: FedoraObject.objects.get(pk='test'),
                                  attachment_model=DocumentAttachment)
