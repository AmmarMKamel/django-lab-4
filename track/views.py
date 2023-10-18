from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Track
from .forms import TrackForm


# Create your views here.
class ListTracks(LoginRequiredMixin, generic.ListView):
    model = Track
    context_object_name = 'tracks'


class DeleteTrack(LoginRequiredMixin, generic.DeleteView):
    model = Track
    success_url = '/tracks'


class CreateTrack(LoginRequiredMixin, generic.CreateView):
    model = Track
    form_class = TrackForm
    success_url = '/tracks'


class UpdateTrack(LoginRequiredMixin, generic.UpdateView):
    model = Track
    fields = ['name']
    success_url = '/tracks'
