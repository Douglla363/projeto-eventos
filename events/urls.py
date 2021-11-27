from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/create/', views.create, name='create'),
    path('events/<int:id>', views.show, name='show'),
    #path('events/', views.store, name='store'),

    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),


    path('dashboard/', views.dashboard, name='dashboard'),
]
