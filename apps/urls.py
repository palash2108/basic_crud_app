from django.urls import include, path
from django.contrib import admin

from theme import views


urlpatterns = [
    path('person_fbv/', include('person_fbv.urls', namespace='person_fbv')),
    path('', views.home),
]
