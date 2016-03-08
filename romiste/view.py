from django.shortcuts import render

from romiste.models import ScientistPerson, RomanyPerson, Place, RomanyThing


def index(req):
    scientists = ScientistPerson.objects.all().order_by('-_fedora_last_modified')[:10]
    respondents = RomanyPerson.objects.all().order_by('-_fedora_last_modified')[:10]
    places = Place.objects.all().order_by('-_fedora_last_modified')[:10]
    recordings = RomanyThing.objects.all().order_by('-_fedora_last_modified')[:10]
    return render(req, 'romiste/index.html', {
        'scientists' : scientists,
        'respondents' : respondents,
        'places' : places,
        'recordings' : recordings
    })