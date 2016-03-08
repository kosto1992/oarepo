from django.shortcuts import render

from romiste.models import ScientistPerson, RomanyPerson, Place, RomanyThing


def index(req):
    scientists = ScientistPerson.objects.all()
    respondents = RomanyPerson.objects.all()
    places = Place.objects.all()
    recordings = RomanyThing.objects.all()
    return render(req, 'romiste/index.html', {
        'scientists' : scientists,
        'respondents' : respondents,
        'places' : places,
        'recordings' : recordings
    })