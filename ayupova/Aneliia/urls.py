from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home', kwargs={'age': '16', 'hobby': 'IT'}),
    path('about', views.about, name='about', kwargs={'sity': 'Neftekamsk', 'study': 'nice'}),
    path('contacts', views.contscts, name='contacts', kwargs={'number': '+89874920177'}),
    re_path(r'^', views.NotFound)
]