from django.conf.urls import url

from photo import views

urlpatterns = [
    url('^$', views.index, name='index'),
]