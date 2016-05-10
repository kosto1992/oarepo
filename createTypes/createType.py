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
from fedoralink_ui.models import ResourceType, Template


class createType:
    def createTemplate(self, pk, type, file):
        model = Template
        parent = FedoraObject.objects.get(pk=pk)
        templateObject = parent.create_child(type, flavour=model)
        templateObject.save()
        templateObject.label = type+'Template'
        stream = TypedStream(file, filename='romiste_scientists_'+type+'.html')

        templateObject.set_template_bitstream(stream)

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
        typeObject.rdf_types = [DC.Object]
        template = self.createTemplate(pk=typeObject.id, type='view', file='./detail.html')
        typeObject.templates_view = template.id
        typeObject.save()

        template = self.createTemplate(pk=typeObject.id, type='edit', file='./edit.html')
        typeObject.templates_edit = template.id
        typeObject.save()

        print(typeObject.pk)

        print('Object %s should be saved', typeObject.label)

create = createType()
create.createType()