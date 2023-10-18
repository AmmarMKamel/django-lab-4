from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTrainee.as_view(), name='list_trainee'),
    path('add/', views.AddTrainee.as_view(), name='add_trainee'),
    path('delete/<int:id>', views.delete_trainee, name='delete_trainee'),
    path('update/<int:id>', views.update_trainee, name='update_trainee'),
]
