# Author GennadySX
# 14.01.2020
import requests
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from bs4 import BeautifulSoup as bs
import re


class Helper:
    def figure(req, default = False):
        base_url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
        x = base_url + str('?')
        if default == False:
            if req['name'] != '':
                x = x + str('searchString=') + str(req['name']) + str('&')
            if req['costFrom'] != 'false':
                x = x + str('priceFromGeneral=') + str(req['costFrom']) + str('&')
            if req['costTo'] != 'false':
                x = x + str('priceToGeneral=') + str(req['costTo']) + str('&')
            if req['sortBy'] != 'false':
                x = x + str('sortBy=') + str(req['sortBy']) + str('&')
            if req['showBy'] != 'false':
                x = x + str('recordsPerPage=') + str(req['showBy'])
        return x


class Parser:
    def pars_gos(uri):
        session = requests.Session()
        request = session.get(uri, headers={'User-Agent': 'Mozilla/5.0'})
        # print('OK')
        soup = bs(request.content, 'lxml')
        items = soup.find_all('div', attrs={'class': 'search-registry-entry-block'})
        links = []
        inx = 0
        for h in items:
            regForm = h.find('div', attrs={'class': 'registry-entry__header-top__title'}).text.strip()
            link = h.find('div', attrs={'class': 'registry-entry__header-mid__number'}).find('a', href=True)['href']
            numberOrder = h.find('div', attrs={'class': 'registry-entry__header-mid__number'}).text.split(',')[ 0].strip()
            #
            typeOrder = h.find('div', attrs={'class': 'registry-entry__header-mid__title'}).text.strip()
            desc = h.find('div', attrs={'class': 'registry-entry__body-value'}).text
            #
            clientBlc = h.find('div', attrs={'class': 'registry-entry__body-href'})
            clientLink = clientBlc.find("a",  href=True)['href']
            clientName = clientBlc.find("a").text
            #
            price = h.find('div', attrs={'class': 'price-block__value'}).text.replace('₽', '').split(',')[0].strip()
            #
            dateBlock = []
            for ds in h.find('div', attrs={'class': 'registry-entry__right-block'}).find('div', attrs={'class': 'data-block'}).find_all('div', attrs={'class', 'data-block__value'}):
                dateBlock.append(ds.text)
            links.insert(inx, (regForm, link, numberOrder, typeOrder, desc, clientLink, clientName, price, dateBlock))
            inx = inx + 1
        return links
