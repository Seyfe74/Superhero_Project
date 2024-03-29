from django.urls import path
from . import views

app_name = 'superheros'
urlpatterns = [
     path ('', views.index, name = 'index'),
     path ('<int:hero_id>/', views.detail , name = 'detail'),
     path ('new/', views.create , name = 'create'),
     path ('<int:hero_id>/d/', views.delete , name = 'delete'),
     path ('<int:hero_id>/e/', views.edit , name = 'edit')
 ]