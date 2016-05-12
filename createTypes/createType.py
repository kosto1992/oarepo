import django

from rdflib.namespace import DC

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.utils import TypedStream

django.setup()

import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

from fedoralink.models import FedoraObject
from fedoralink_ui.models import ResourceType, Template, ResourceFieldType


class createType:
    def createTemplate(self, pk, type, file):
        model = Template
        parent = FedoraObject.objects.get(pk=pk)
        templateObject = parent.create_child(type, flavour=model)
        templateObject.label = type+'Template'
        stream = TypedStream(file, filename='romiste_scientists_'+type+'.html')

        templateObject.set_local_bitstream(stream)

        templateObject.save()
        return templateObject

    def createType(self):
        model = ResourceType
        parent = FedoraObject.objects.get(pk='type')
        typeObject = parent.create_child('edit', flavour=model)
        typeObject.save()
        #typeObject = FedoraObject.objects.get(pk='type/64/94/59/35/64945935-9644-4d4e-a8da-bde34891e9b1')

        typeObject.label = 'TestType'
        typeObject.controller = 'Controller'
        typeObject.rdf_types = ["http://cesnet.cz/ns/repository#DCTermsCollection"]
        template = self.createTemplate(pk=typeObject.id, type='view', file='./collection_detail.html')
        typeObject.template_view = template
        typeObject.save()

        template = self.createTemplate(pk=typeObject.id, type='edit', file='./edit.html')
        typeObject.template_edit = template
        typeObject.save()

        print(typeObject.pk)

        print('Object %s should be saved', typeObject.label)

    def createResourceFieldType(self):
        model = ResourceFieldType
        parent = FedoraObject.objects.get(pk='type')
        typeObject = parent.create_child('view', flavour=model)
        typeObject.label = "ResourceFieldType"
        typeObject.field_fedoralink_type = "fedoralink.indexer.fields.IndexedLanguageField"
        typeObject.field_name = 'title'

        typeObject.resource_type = FedoraObject.objects.get(pk='type/95/36/d6/8f/9536d68f-9b6d-43d0-9a07-7764aca2f009')

        typeObject.save()

        template = self.createTemplate(pk=typeObject.id, type='view', file='./test_title.html')
        typeObject.template_field_detail_view = template
        typeObject.save()


create = createType()
# create.createType()
create.createResourceFieldType()