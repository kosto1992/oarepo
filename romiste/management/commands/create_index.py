# encoding: utf-8

from __future__ import unicode_literals
from django.core.management import call_command

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Nahraje transformace do fedory repozitare'

    def handle(self, *args, **options):
        call_command('config_repository_index_elasticsearch', 'fedoralink.common_namespaces.dc.DCObject')
        call_command('config_repository_index_elasticsearch', 'dcterms.models.DocumentAttachment')
        call_command('config_repository_index_elasticsearch', 'romiste.models.Image')
        call_command('config_repository_index_elasticsearch', 'romiste.models.ScientistPerson')
        call_command('config_repository_index_elasticsearch', 'romiste.models.RomanyPerson')
        call_command('config_repository_index_elasticsearch', 'romiste.models.Place')
        call_command('config_repository_index_elasticsearch', 'romiste.models.Thing')
        call_command('config_repository_index_elasticsearch', 'romiste.models.RomanyThing')
        call_command('config_repository_index_elasticsearch', 'romiste.models.Tag')
        call_command('config_repository_index_elasticsearch', 'romiste.models.Event')
