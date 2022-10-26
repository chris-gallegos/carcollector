from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_show/', views.add_show, name='add_show'),
    path('mods/', views.ModList.as_view(), name='mods_index'),  # mods start here
    path('mods/<int:pk>/', views.ModDetail.as_view(), name='mods_detail'),
    path('mods/create/', views.ModCreate.as_view(), name='mods_create'),
    path('mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mods_update'),
    path('mods/<int:pk>/delete/', views.ModDelete.as_view(), name='mods_delete'),
    path('cars/<int:car_id>/assoc_mod/<int:mod_id>/', views.assoc_mod, name='assoc_mod'),
]
