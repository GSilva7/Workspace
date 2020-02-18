from django.urls import path
from . import views

urlpatterns = [
    path('', views.GmudList, name='gmud_list'),
    path('create/', views.GmudCreate, name='gmud_create'),
    path('view/<int:pk>', views.GmudView, name='gmud_view'),
    path('update/<int:pk>', views.GmudUpdate, name='gmud_update'),
    path('delete/<int:pk>', views.GmudDelete, name='gmud_delete'),
]