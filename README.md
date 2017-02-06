# oarepo readme
OARepo dcterms

nastavenie virtualenv:
* Django 1.9
* pip
* fedoralink (pip install -e /path/to/local/fedoralink/directory)
* bleach
* django-bootstrap-pagination
* django-bootstrap3
* html5lib
* inflection
* isodate
* pyparsing
* python-dateutil
* rdflib
* requests
* setuptools
* six
* wheel

Instalacia fedoralinku v aktivnom virtenv.

Settings.py:
Nastavenie ALLOWED_HOSTS
    DATABASES (postgresql)
    STATIC_ROOT = '/apache/static'

Nastavit pristupove udaje v oarepo/admin_auth.cfg (FEDORA_ADMIN pristup)

Spustit manage.py migrate (nastavenie DB)
manage.py collect_static

