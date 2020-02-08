from django.conf.urls import url
from skillreader import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name='index'),
]