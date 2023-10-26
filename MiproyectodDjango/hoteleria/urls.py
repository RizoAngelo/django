from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('verpersona', views.verpersona, name='verpersona'),
    path('verpersona/crearpersona', views.crearpersona, name='crearpersona'),
    path('verpersona/editarpersona', views.editarpersona, name='editarpersona'),
    
]