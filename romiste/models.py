from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from rdflib.namespace import FOAF

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import EBUCORE, FEDORA, CESNET
from fedoralink.indexer import IndexedField, TEXT, STRING, MULTI_VAL, DATE
from fedoralink.models import IndexableFedoraObject
from fedoralink.type_manager import FedoraTypeManager


class ScientistPerson(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('firstName', FOAF.firstName, stored=True, indexed=True, type=TEXT, prefix='foaf_',
                     required=True, verbose_name=_('Jméno (foaf)')),
        IndexedField('surname', FOAF.surname, stored=True, indexed=True, type=TEXT, prefix='foaf_',
                     verbose_name=_('Přijmení (foaf)')),
        IndexedField('middlename', CESNET.middlename, stored=True, indexed=True, type=TEXT, prefix='cesnet_',
                     verbose_name=_('Střední jméno ()')),
        IndexedField('nickname', FOAF.nickname, stored=True, indexed=True, type=STRING, prefix='foaf_',
                     verbose_name=_('Nickname (foaf)')),
        IndexedField('titles', CESNET.titles, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Tituly ()')),
        IndexedField('degrees', CESNET.degrees, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Degrees ()')),
        IndexedField('gender', CESNET.gender, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Pohlaví ()')),
        IndexedField('nationality', CESNET.nationality, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Národnost ()')),
        IndexedField('language', CESNET.language, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Jazyk ()')),
        IndexedField('birthday', CESNET.birthday, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Datum narození ()')),
        IndexedField('birthplace', CESNET.birthplace, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Místo narození ()')),
        IndexedField('deathday', CESNET.deathday, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Datum úmrtí ()')),
        IndexedField('deathplace', CESNET.deathplace, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Místo úmrtí ()')),
        IndexedField('phone', CESNET.phone, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Telefonní číslo ()')),
        IndexedField('email', CESNET.email, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Email ()')),
        IndexedField('web', CESNET.web, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Web ()')),
        IndexedField('photo', CESNET.photo, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Foto ()')),
        IndexedField('notes', CESNET.notes, stored=True, indexed=True, type=TEXT, prefix='cesnet_',
                     verbose_name=_('Poznámka ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.ScientistPerson)

FedoraTypeManager.register_model(ScientistPerson, on_rdf_type=[CESNET.ScientistPerson])