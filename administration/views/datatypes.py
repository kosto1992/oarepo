from django.views.generic import TemplateView

from fedoralink.type_manager import FedoraTypeManager
from fedoralink_ui.models import ResourceType


class IndexView(TemplateView):
    template_name = 'oarepo/administration/datatypes/index.html'

    # noinspection PyProtectedMember
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for model in FedoraTypeManager.models:
            print('model:', model)
            print("    application: ", model._meta.application)
            print("    rdf types: ", model._meta.rdf_types)
            print("    fields: ")
            for field in model._meta.fields:
                print('        %s (%s)' % (field.name, field.rdf_name))

        for rt in ResourceType.objects.all():
            print("resource type: ", rt.label)
            print("    view template", rt.template_view)

            if rt.template_view:
                template_bitstream = rt.template_view.get_bitstream()
                bitstream_data = template_bitstream.stream.read().decode('utf-8')
                print("        ", template_bitstream, bitstream_data[:60].replace('\n', '\\n'))

            print("    edit template", rt.template_edit)
            print("    list item template", rt.template_list_item)

        return context
