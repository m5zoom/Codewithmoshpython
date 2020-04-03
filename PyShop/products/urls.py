from django.conf.urls import url
from . import views

#
# /products/1/detail
# /products/new/

urlpatterns = [
    url('', views.index),
    url('new', views.new)
]
