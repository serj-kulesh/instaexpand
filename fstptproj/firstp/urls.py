from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_session', views.test_session, name='test_session'),
    re_path(r'^request/(?P<method>[a-zA-Z0-9_-]+)$', views.method_processor, name='method_processor')
    
]
