from django.urls import path

from person_fbv import views

app_name = 'person_fbv'

#This links the URLs of different web pages which are being used in the app
urlpatterns = [
  path('', views.person_list, name='person_list'),
  path('new', views.person_create, name='person_new'),
  path('edit/<int:pk>', views.person_update, name='person_edit'),
  path('delete/<int:pk>', views.person_delete, name='person_delete'),
]