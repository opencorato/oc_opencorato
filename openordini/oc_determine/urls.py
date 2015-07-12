from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf import settings

from open_municipio.urls import *
from open_municipio.om.views import HomeView
from .views import DeterminaDetailView, OOActSearchView

# place app url patterns here
urlpatterns = patterns('',
    url(r'^$', OOActSearchView(template='acts/act_search.html'), name='om_act_search'),
	url(r'^determina/(?P<slug>[-\w]+)/$', DeterminaDetailView.as_view(), name='oo_determina_detail'),
    url(r'^determina/(?P<slug>[-\w]+)/(?P<tab>documents)/$', DeterminaDetailView.as_view(), name='om_determina_detail_documents'),
)