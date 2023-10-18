from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_instructors, name='list_instructors'),
    path('add/', views.add_instructor, name='add_instructor'),
    path('delete/<int:id>', views.delete_instructor, name='delete_instructor'),
    path('update/<int:id>', views.update_instructor, name='update_instructor'),
]
