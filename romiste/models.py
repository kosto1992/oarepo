from django.utils.translation import ugettext_lazy as _

# Create your models here.
from rdflib.namespace import FOAF

from fedoralink.common_namespaces.dc import DCObject
from fedoralink.fedorans import CESNET
from fedoralink.indexer.fields import IndexedTextField, IndexedDateField, IndexedLinkedField, IndexedBinaryField, \
    IndexedGPSField
from fedoralink.indexer.models import IndexableFedoraObject


class Image(DCObject):

    class Meta:
        rdf_types = (CESNET.Image, )


class Video(DCObject):

    class Meta:
        rdf_types = (CESNET.Video, )

class ScientistPerson(IndexableFedoraObject):
    orcid = IndexedTextField(CESNET.orcid, verbose_name=_('Orcid'))
    firstName = IndexedTextField(FOAF.firstName, required=True, verbose_name=_('First name'))
    surname = IndexedTextField(FOAF.surname, required=True, verbose_name=_('Surname'))
    middlename = IndexedTextField(CESNET.middlename, verbose_name=_('Middle name'))
    nickname = IndexedTextField(FOAF.nickname, verbose_name=_('Nickname'))
    titles = IndexedTextField(CESNET.titles, multi_valued=True, verbose_name=_('Titles ()'))       # TODO
    degrees = IndexedTextField(CESNET.degrees, multi_valued=True, verbose_name=_('Degrees ()'))    # TODO
    gender = IndexedTextField(CESNET.gender, verbose_name=_('Gender'))
    nationality = IndexedTextField(CESNET.nationality, verbose_name=_('Nationality'))
    language = IndexedTextField(CESNET.language, verbose_name=_('Primary language'))
    birthday = IndexedDateField(CESNET.birthday, verbose_name=_('Date of Birth'))
    birthplace = IndexedTextField(CESNET.birthplace, verbose_name=_('Birthplace'))
    deathday = IndexedDateField(CESNET.deathday, verbose_name=_('Date of Death'))
    deathplace = IndexedTextField(CESNET.deathplace, verbose_name=_('Place of Death'))
    phone = IndexedTextField(CESNET.phone, multi_valued=True, verbose_name=_('Phone number'))
    email = IndexedTextField(CESNET.email, multi_valued=True, verbose_name=_('Email'))
    web = IndexedTextField(CESNET.web, multi_valued=True, verbose_name=_('Web page'))
    photo = IndexedBinaryField(CESNET.photo, verbose_name=_('Photo'), model=Image)
    notes = IndexedTextField(CESNET.notes, verbose_name=_('Notes'), attrs={"presentation": "textarea"})

    class Meta:
        rdf_types = (CESNET.ScientistPerson, )


class RomanyPerson(IndexableFedoraObject):
    orcid = IndexedTextField(CESNET.orcid, verbose_name=_('Orcid'))
    firstName = IndexedTextField(FOAF.firstName, required=True, verbose_name=_('First name'))
    surname = IndexedTextField(FOAF.surname, required=True, verbose_name=_('Surname'))
    middlename = IndexedTextField(CESNET.middlename, verbose_name=_('Middle name'))
    nickname = IndexedTextField(FOAF.nickname, verbose_name=_('Nickname'))
    titles = IndexedTextField(CESNET.titles, multi_valued=True, verbose_name=_('Titles ()'))       # TODO
    degrees = IndexedTextField(CESNET.degrees, multi_valued=True, verbose_name=_('Degrees ()'))    # TODO
    gender = IndexedTextField(CESNET.gender, verbose_name=_('Gender'))
    nationality = IndexedTextField(CESNET.nationality, verbose_name=_('Nationality'))
    language = IndexedTextField(CESNET.language, multi_valued=True, verbose_name=_('Primary language'))
    birthday = IndexedDateField(CESNET.birthday, verbose_name=_('Date of Birth'))
    birthplace = IndexedTextField(CESNET.birthplace, verbose_name=_('Birthplace'))
    deathday = IndexedDateField(CESNET.deathday, verbose_name=_('Date of Death'))
    deathplace = IndexedTextField(CESNET.deathplace, verbose_name=_('Place of death'))
    phone = IndexedTextField(CESNET.phone, multi_valued=True, verbose_name=_('Phone number'))
    email = IndexedTextField(CESNET.email, multi_valued=True, verbose_name=_('Email'))
    web = IndexedTextField(CESNET.web, multi_valued=True, verbose_name=_('Web page'))
    photo = IndexedBinaryField(CESNET.photo, verbose_name=_('Photo'), model=Image)
    notes = IndexedTextField(CESNET.notes, verbose_name=_('Notes'), attrs={"presentation": "textarea"})

    dialect = IndexedTextField(CESNET.dialect, verbose_name=_('Dialect'))
    parent = IndexedTextField(CESNET.parent, multi_valued=True, verbose_name=_('Parent'))
    child  = IndexedTextField(CESNET.child, multi_valued=True, verbose_name=_('Child'))

    class Meta:
        rdf_types = (CESNET.RomanyPerson, )


class Place(IndexableFedoraObject):
    title = IndexedTextField(CESNET.title, required=True, verbose_name=_('Place name'))
    title_alt = IndexedTextField(CESNET.title_alt, multi_valued=True, verbose_name=_('Alternative name'))
    street = IndexedTextField(CESNET.street, verbose_name=_('Street'))
    house_number = IndexedTextField(CESNET.house_number, verbose_name=_('House number'))
    zip = IndexedTextField(CESNET.zip, verbose_name=_('ZIP code'))
    district = IndexedTextField(CESNET.district, verbose_name=_('District'))
    region = IndexedTextField(CESNET.region, verbose_name=_('Region'))
    country = IndexedTextField(CESNET.country, verbose_name=_('Country'))
    gps = IndexedGPSField(CESNET.gps, verbose_name=_('GPS'), help_text=_('Lattitude and longitude, separated with ; or ,'))
    photo = IndexedTextField(CESNET.photo, verbose_name=_('Photo'))
    notes = IndexedTextField(CESNET.notes, verbose_name=_('Notes'), attrs={'presentation': 'textarea'})

    language = IndexedTextField(CESNET.language, multi_valued=True, verbose_name=_('Language'))
    dialect = IndexedTextField(CESNET.dialect, verbose_name=_('Dialect'))
    title_romany = IndexedTextField(CESNET.title_romany, verbose_name=_('Place name (Romani)'))
    title_alt_romany = IndexedTextField(CESNET.title_alt_romany, verbose_name=_('Alternative name (Romani)'))

    class Meta:
        rdf_types = (CESNET.Place, )


class Thing(IndexableFedoraObject):
    title = IndexedTextField(CESNET.title, required=True, verbose_name=_('Title'))
    creator = IndexedTextField(CESNET.creator, verbose_name=_('Creator'))
    creation_date = IndexedDateField(CESNET.creation_date, verbose_name=_('Creation Date'))
    creation_place = IndexedTextField(CESNET.creation_place, verbose_name=_('Creation Place'))
    keyword = IndexedTextField(CESNET.keyword, multi_valued=True, verbose_name=_('Keywords'))
    description = IndexedTextField(CESNET.description, verbose_name=_('Description'),
                                   attrs={'presentation': 'textarea'})

    class Meta:
        rdf_types = (CESNET.Thing, )


class RomanyThing(IndexableFedoraObject):
    title = IndexedTextField(CESNET.title, required=True, verbose_name=_('Title'))
    creator = IndexedTextField(CESNET.creator, verbose_name=_('Creator'))
    creation_date = IndexedDateField(CESNET.creation_date, verbose_name=_('Creation Date'))
    creation_place = IndexedTextField(CESNET.creation_place, verbose_name=_('Creation Place'))
    keyword = IndexedTextField(CESNET.keyword, multi_valued=True, verbose_name=_('Keywords'))
    description = IndexedTextField(CESNET.description, verbose_name=_('Description'),
                                   attrs={'presentation': 'textarea'})

    respondent = IndexedTextField(CESNET.respondent, verbose_name=_('Respondent'))
    circumstance = IndexedTextField(CESNET.circumstance, verbose_name=_('Circumstance'))
    video = IndexedBinaryField(CESNET.video, verbose_name=_('Record'), model=Video)
    record_type = IndexedTextField(CESNET.record_type, verbose_name=_('Recording Type'))
    technical_notes = IndexedTextField(CESNET.technical_notes, verbose_name=_('Technical Notes'),
                                       attrs={'presentation': 'textarea'})

    class Meta:
        rdf_types = (CESNET.RomanyThing, )


class Tag(IndexableFedoraObject):
    title = IndexedTextField(CESNET.title, required=True, verbose_name=_('Tag name'))

    class Meta:
        rdf_types = (CESNET.Tag, )


class Event(IndexableFedoraObject):
    title = IndexedTextField(CESNET.title, required=True, verbose_name=_('Title'))
    date_from = IndexedDateField(CESNET.date_from, verbose_name=_('Start'))
    date_to = IndexedDateField(CESNET.date_to, verbose_name=_('End'))
    place = IndexedTextField(CESNET.place, verbose_name=_('Place'))
    actor = IndexedTextField(CESNET.actor, verbose_name=_('Actor'))
    description = IndexedTextField(CESNET.description, verbose_name=_('Description'))

    class Meta:
        rdf_types = (CESNET.Event, )
