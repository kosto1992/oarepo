from django.shortcuts import render


def index(req):
    return render(req, 'baseOArepo/index.html', {
    })
