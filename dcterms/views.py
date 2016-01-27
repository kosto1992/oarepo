from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, FileResponse

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import EBUCORE
from rdflib.namespace import DC

from dcterms.models import DocumentAttachment

# Create your views here.
from fedoralink.models import FedoraObject


def index(req):
    return HttpResponseRedirect(reverse('dcterms:rozsirene_hledani', kwargs={'parametry': ''}))

# def detail(req, id):
#     doc = DCObject.objects.get(pk='test/' + id.replace('_', '/'))
#     # dokumenty = [AccreditationDocumentAttachment.objects.get(pk=x) for x in doc.attachments]
#     # attachmentsdokumenty.sort(key=lambda x: str(x.title))
#     childrens = doc.children
#
#     #print(EBUCORE.filename)
#     file = DocumentAttachment.objects.get(pk='test/' + id.replace('_', '/'))
#
#     return render(req, 'dcterms/detail.html', {
#         'item' : doc,
#         'item_id' : id,
#         'childrens' : childrens,
#         'documents' : file
#         # 'documents' : dokumenty
#     })

def download(req, bitstream_id):
    attachment = DocumentAttachment.objects.get(pk='test/' + bitstream_id.replace('_', '/'))

    bitstream = attachment.get_bitstream()
    resp = FileResponse(bitstream.stream, content_type=bitstream.mimetype)
    resp['Content-Disposition'] = 'inline; filename="'+attachment.filename
    return resp