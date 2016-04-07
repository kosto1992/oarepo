import django

django.setup()

import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

from fedoralink.models import FedoraObject
from fedoralink_ui.models import Type, Template


class createType:
    def createTemplate(self):
        model = Template
        parent = FedoraObject.objects.get(pk='types')
        templateObject = parent.create_child('', flavour=model)
        templateObject.save()
        templateObject.label = 'ViewTemplate'
        f = open('../romiste/templates/romiste/scientists/detail.html')

        templateObject.set_template_bitstream(f)

        templateObject.save()
        return templateObject.id

    def createType(self, templateId):
        model = Type
        parent = FedoraObject.objects.get(pk='types')
        typeObject = parent.create_child('', flavour=model)
        typeObject.save()

        typeObject.label = 'TestType'
        typeObject.controller = 'Controller'
        template = FedoraObject.objects.get(pk=templateId)
        typeObject.templates_view = template.id
        typeObject.save()

        print(typeObject.pk)

        objectb = Type.objects.get(pk=typeObject.pk)

        print(objectb.label)

        print('Object %s should be saved', typeObject.label)

create = createType()
template = create.createTemplate()
create.createType(templateId=template)