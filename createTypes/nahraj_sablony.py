import django
import re

from rdflib.namespace import DC

from fedoralink.authentication.Credentials import Credentials
from fedoralink.authentication.as_user import as_user
from fedoralink.fedorans import CIS, CESNET, CESNET_TYPE
from fedoralink.models import FedoraObject
from fedoralink.utils import TypedStream
from fedoralink_ui.models import ResourceType, Template, ResourceCollectionType
django.setup()


def vytvor_nebo_aktualizuj_sablonu(resource_type, objekt_sablony, typ_sablony, file):
    if not objekt_sablony:
        objekt_sablony = resource_type.create_child(typ_sablony, flavour=Template, slug=typ_sablony)
        objekt_sablony.label = typ_sablony + 'Template'

    stream = TypedStream(file)
    objekt_sablony.set_local_bitstream(stream)
    objekt_sablony.save()
    return objekt_sablony


# def vytvor_adresare():
#     try:
#         FedoraObject.objects.get(pk='administration/resource-types')
#     except:
#         parent = FedoraObject.objects.get(pk='')
#         administration = parent.create_child('administration', slug='administration')
#         administration.save()
#         resource_types = administration.create_child('resource-types', slug='resource-types')
#         resource_types.save()


def importuj_typ(typ, nastaveni):
    parent = FedoraObject.objects.get(pk='administration/types')
    for c in parent.children:
        print(typ, c.rdf_types, type(c.rdf_types), typ in c.rdf_types)
        if typ in c.rdf_types:
            resource_type = c
            resource_type.update()
            break
    else:
        resource_type = parent.create_child(str(typ), flavour=ResourceType,
                                            slug=re.sub('[^a-zA-Z0-9]', '-', typ))
        resource_type.save()

    resource_type.label = str(typ)
    resource_type.controller = nastaveni.get('controller', None)
    resource_type.fedoralink_model = nastaveni.get('fedoralink_model', None)
    resource_type.rdf_types = [typ]

    for typ_sablony in 'view', 'edit', 'list_item':
        if typ_sablony in nastaveni:
            template = getattr(resource_type, 'template_' + typ_sablony)
            template = vytvor_nebo_aktualizuj_sablonu(resource_type, template,
                                                      typ_sablony=typ_sablony, file=nastaveni[typ_sablony])
            setattr(resource_type, 'template_' + typ_sablony, template)

    resource_type.save()


def importuj_kolekci(typ, nastaveni):
    parent = FedoraObject.objects.get(pk='administration/types')
    for c in parent.children:
        if not isinstance(c, ResourceCollectionType):
            continue
        print(typ, c.rdf_types, type(c.rdf_types), typ in c.rdf_types)
        if typ in c.rdf_types:
            collection_type = c
            collection_type.update()
            break
    else:
        collection_type = parent.create_child(str(typ), flavour=ResourceCollectionType,
                                              slug=re.sub('[^a-zA-Z0-9]', '-', typ))
        collection_type.save()

    collection_type.label = str(typ)
    collection_type.controller = nastaveni.get('controller', None)
    collection_type.fedoralink_model = nastaveni.get('fedoralink_model', None)
    collection_type.rdf_types = [typ]

    collection_type.save()

    for typ_sablony in ('search','view', 'edit', 'list_item'):
        if typ_sablony in nastaveni:
            template = getattr(collection_type, 'template_' + typ_sablony)
            template = vytvor_nebo_aktualizuj_sablonu(collection_type, template,
                                                      typ_sablony=typ_sablony, file=nastaveni[typ_sablony])
            setattr(collection_type, 'template_' + typ_sablony, template)

    if 'primary_child_type' in nastaveni:
        collection_type.primary_child_type = \
            ResourceType.objects.get(rdf_types=nastaveni['primary_child_type'])

    if 'primary_subcollection_type' in nastaveni:
        collection_type.primary_subcollection_type = \
            ResourceType.objects.get(rdf_types=nastaveni['primary_subcollection_type'])

    collection_type.save()


def importuj(sablony, kolekce):
    for typ, nastaveni in sablony.items():
        importuj_typ(typ, nastaveni)
    for typ, nastaveni in kolekce.items():
        importuj_kolekci(typ, nastaveni)

# vytvor_adresare()
import configparser
config = configparser.ConfigParser()
config.read('../oarepo/admin_auth.cfg')

credentials = Credentials(config['oarepo']['admin'],config['oarepo']['admin_pw'])
print("user:" + credentials.username)
with as_user(credentials):
    importuj(
        {
            DC.Object: {
                'view' : 'detail.html',
                'edit' : 'edit.html',
                'fedoralink_model' : 'fedoralink.common_namespaces.dc.DCObject'
            },
            CESNET.DCObjectWithAttachment: {
                'view' : 'detail.html',
                'edit' : 'edit.html',
                'fedoralink_model' : 'baseOArepo.models.DCObjectWithAttachment'
            },
            CESNET_TYPE.ResourceTypeCollection: {
                'list_item' : 'administration_search_result_row.html',
                'fedoralink_model' : 'fedoralink_ui.models.ResourceTypeCollection'
            }
            # CIS.AccreditationDocument: {
            #     'view'      : 'templates_to_upload/accreditation_documents/view.html',
            #     'list_item' : 'templates_to_upload/accreditation_documents/list_item.html',
            #     'fedoralink_model': 'akreditacni_dokumenty.models.AccreditationDocument'
            # },
            # CIS.QualificationWorkTypeCollection: {
            #     'view'      : 'templates_to_upload/theses/druh.html',
            # },
            # CIS.QualificationWorkFacultyCollection: {
            #     'view': 'templates_to_upload/theses/fakulta.html',
            # },
            # CIS.QualificationWorkYearCollection: {
            #     'view': 'templates_to_upload/theses/rok.html',
            # },
            # CIS.QualificationWorkFieldCollection: {
            #     'view': 'templates_to_upload/theses/obor.html',
            # },
            # CIS.QualificationWork: {
            #     'view': 'templates_to_upload/theses/detail.html',
            # }
        },
        {
            CESNET.DCTermsCollection: {
                'primary_child_type': DC.Object,
                'primary_subcollection_type': CESNET.DCTermsCollection,
                'view' : 'collection_detail.html',
                'fedoralink_model' : 'fedoralink_ui.models.DCTermsCollection'
            },
            CESNET.AttachmentsCollection: {
                'primary_child_type': CESNET.DCObjectWithAttachment,
                'primary_subcollection_type': CESNET.AttachmentsCollection,
                'view' : 'collection_detail.html',
                'fedoralink_model' : 'baseOArepo.models.AttachmentsCollection'
            },
            CESNET_TYPE.AdministrationCollection: {
                'view' : 'administration_collection_detail.html',
                'fedoralink_model' : 'fedoralink_ui.models.AdministrationCollection'
            }
        })
