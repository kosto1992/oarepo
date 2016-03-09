from django.shortcuts import render


def index(req):
    return render(req, 'state_engine/index.html')

def index_romiste(req):
    return render(req, 'state_engine/index_romiste.html')
