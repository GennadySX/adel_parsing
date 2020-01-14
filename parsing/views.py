from django.shortcuts import render
from django.views.generic import TemplateView
from parsing.helper import *


# Create your views here.
class MainView(TemplateView):
    def index(request):
        base_url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?'
        return render(request, 'main/index.html')

    def formCatch(request):
        if request.method == 'POST':
            return True
        return False

    def getValue(request):
        base_url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
        data = Helper.figure(base_url, request.GET)
        return render(request, 'cost.html', {'gets': data})

    def parser(request):
        base_url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
        data = Parser.pars_gos(base_url)
        return render(request, 'main/index.html ', {'data': data})








