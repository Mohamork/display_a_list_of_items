from django.urls import path
from . import views
urlpatterns = [
path('series/',views.get_series,name='series')
]