from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from elasticsearch import Elasticsearch

es = Elasticsearch('http://swj.myds.me:9200')


class HomeView(TemplateView):
    template_name = 'search/home.html'


class SearchView(TemplateView):
    template_name = 'search/result.html'


def search_helper(request):
    return
