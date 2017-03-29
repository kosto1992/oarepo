from django.views.generic import TemplateView

from fedoralink.type_manager import FedoraTypeManager


class IndexView(TemplateView):
    template_name = 'oarepo/administration/datatypes/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for model in FedoraTypeManager.models:
            print('model:', model)
            for field in model._meta.fields:
                print('    %s (%s)' % (field.name, field.rdf_name))
        return context