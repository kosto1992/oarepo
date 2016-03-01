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
        IndexedField('orcid', CESNET.orcid, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Orcid ()')),
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

class RomanyPerson(IndexableFedoraObject):
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
        IndexedField('dialect', CESNET.dialect, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Dialekt ()')),
        IndexedField('child_of', CESNET.child_of, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Dítě ()')),
        IndexedField('parent_of', CESNET.child_of, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Rodič ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.RomanyPerson)

FedoraTypeManager.register_model(RomanyPerson, on_rdf_type=[CESNET.RomanyPerson])

class Place(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('title', CESNET.title, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     required=True, verbose_name=_('Název ()')),
        IndexedField('title_alt', CESNET.title_alt, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Alternativní název/Tag ()')),
        IndexedField('street', CESNET.street, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Ulice ()')),
        IndexedField('land_registry_number', CESNET.land_registry_number, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Číslo krajiny ()')),
        IndexedField('house_number', CESNET.house_number, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Popisné číslo ()')),
        IndexedField('zip', CESNET.zip, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('PSČ ()')),
        IndexedField('district', CESNET.district, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Okres ()')),
        IndexedField('region', CESNET.region, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Kraj ()')),
        IndexedField('country', CESNET.country, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Štát ()')),
        IndexedField('gps', CESNET.gps, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('GPS ()')),
        IndexedField('photo', CESNET.photo, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Fotka ()')),
        IndexedField('notes', CESNET.notes, stored=True, indexed=True, type=TEXT, prefix='cesnet_',
                     verbose_name=_('Poznámky ()')),

        IndexedField('language', CESNET.language, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Jazyk ()')),
        IndexedField('dialect', CESNET.dialect, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Dialekt ()')),
        IndexedField('title_romany', CESNET.title_romany, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Rómsky název ()')),
        IndexedField('title_alt_romany', CESNET.title_alt_romany, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Alternativní rómsky název ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.Place)

FedoraTypeManager.register_model(Place, on_rdf_type=[CESNET.Place])

class Thing(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('title', CESNET.title, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     required=True, verbose_name=_('Název ()')),
        IndexedField('creator', CESNET.creator, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Autor ()')),
        IndexedField('creation_date', CESNET.creation_date, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Datum vytvoření ()')),
        IndexedField('creation_place', CESNET.creation_place, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Místo vytvoření ()')),
        IndexedField('keyword', CESNET.keyword, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Klíčová slova ()')),
        IndexedField('description', CESNET.description, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Popis ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.Thing)

FedoraTypeManager.register_model(Thing, on_rdf_type=[CESNET.Thing])

class RomanyThing(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('title', CESNET.title, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     required=True, verbose_name=_('Název ()')),
        IndexedField('creator', CESNET.creator, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Autor ()')),
        IndexedField('creation_date', CESNET.creation_date, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Datum vytvoření ()')),
        IndexedField('creation_place', CESNET.creation_place, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Místo vytvoření ()')),
        IndexedField('keyword', CESNET.keyword, stored=True, indexed=True, type=MULTI_VAL | STRING, prefix='cesnet_',
                     verbose_name=_('Klíčová slova ()')),
        IndexedField('description', CESNET.description, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Popis ()')),
        IndexedField('respondent', CESNET.respondent, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Respondent ()')),
        IndexedField('circumstance', CESNET.circumstance, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Okolnosti ()')),
        IndexedField('record_type', CESNET.record_type, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Typ nahrávky ()')),
        IndexedField('technical_notes', CESNET.technical_notes, stored=True, indexed=True, type=TEXT, prefix='cesnet_',
                     verbose_name=_('Technické poznámky ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.RomanyThing)

FedoraTypeManager.register_model(RomanyThing, on_rdf_type=[CESNET.RomanyThing])

class Tag(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('title', CESNET.title, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     required=True, verbose_name=_('Název ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.Tag)

FedoraTypeManager.register_model(Tag, on_rdf_type=[CESNET.Tag])

class Event(IndexableFedoraObject):
    indexed_fields = [
        IndexedField('title', CESNET.title, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     required=True, verbose_name=_('Název ()')),
        IndexedField('date_from', CESNET.date_from, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Od ()')),
        IndexedField('date_to', CESNET.date_to, stored=True, indexed=True, type=DATE, prefix='cesnet_',
                     verbose_name=_('Do ()')),
        IndexedField('place', CESNET.place, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Místo ()')),
        IndexedField('actor', CESNET.actor, stored=True, indexed=True, type=STRING, prefix='cesnet_',
                     verbose_name=_('Herec ()')),
        IndexedField('description', CESNET.description, stored=True, indexed=True, type=TEXT, prefix='cesnet_',
                     verbose_name=_('Popis ()')),
    ]

    def created(self):
        super().created()
        self.types.add(CESNET.Event)

FedoraTypeManager.register_model(Event, on_rdf_type=[CESNET.Event])