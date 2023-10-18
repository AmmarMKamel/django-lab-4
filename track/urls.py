from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTracks.as_view(), name='track.list'),
    path('delete/<int:pk>', views.DeleteTrack.as_view(), name='track.delete'),
    path('update/<int:pk>', views.UpdateTrack.as_view(), name='track.update'),
    path('add', views.CreateTrack.as_view(), name='track.add'),
]