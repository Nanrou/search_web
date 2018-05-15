from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.utils.safestring import mark_safe

from elasticsearch import Elasticsearch


# es = Elasticsearch('http://swj.myds.me:9200')

def fake_es(sc):
    return [{'title': sc + str(i), 'content': sc * 200, 'url': 'http://test.shuiwujia.cn/{}'.format(sc),
             'time': datetime.now()} for i in range(30)]


class HomeView(TemplateView):
    template_name = 'search/home.html'


class SearchView(ListView):
    template_name = 'search/result.html'
    context_object_name = 'sc'
    paginate_by = 5

    def get_queryset(self):
        return fake_es(self.request.GET['sc'])

    def get_context_data(self, **kwargs):
        content = super().get_context_data()
        content['raw_paginator'] = mark_safe("""\
        <el-pagination
        layout="prev, pager, next"
        :page-size="{}"
        :current-page="{}"
        :total="{}">
        </el-pagination>
         """.format(8, content['page_obj'].number, content['paginator'].num_pages))
        # es.search(index='test2', q=sc)
        return content


def search_helper(request):
    return
