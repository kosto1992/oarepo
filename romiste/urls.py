from baseOArepo.generic_urls import repository_patterns
from fedoralink.models import FedoraObject
from romiste.models import ScientistPerson
from django.utils.translation import ugettext_lazy as _

urlpatterns = repository_patterns(app_name = 'romiste', model=ScientistPerson,
                        search_facets=[
                            ('surname', _('Dle jmena')),
                        ],
                        search_orderings=(
                                ('surname', _('Dle jmena')),
                        ),
                        search_default_ordering='surname',
                                  add_parent_collection=lambda x: FedoraObject.objects.get(pk='test'),
                                  attachment_model=None)
