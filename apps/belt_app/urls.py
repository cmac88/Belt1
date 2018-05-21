from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^destination/(?P<id>[0-9]+)$', views.destination),
    url(r'^join/(?P<id>[0-9]+)$', views.join),
]      