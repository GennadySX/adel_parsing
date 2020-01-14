from django.shortcuts import render
from django.views.generic import TemplateView
from parsing.helper import *


# Create your views here.
class MainView(TemplateView):
    def index(request):
        uri = Helper.figure(request.GET, True)
        data = Parser.pars_gos(uri)
        dataLen = len(data)
        return render(request, 'main/index.html', {'data': data, 'length': dataLen})

    def getValue(request):
        uri = Helper.figure(request.GET)
        data = Parser.pars_gos(uri)
        dataLen = len(data)
        return render(request, 'main/index.html', {'data': data, 'length': dataLen})










