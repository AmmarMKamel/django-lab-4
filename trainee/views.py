from django.shortcuts import render
from django import views
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Trainee
from .forms import TraineeForm
from track.models import Track


# Create your views here.
class ListTrainee(LoginRequiredMixin, views.View):
    def get(self, req):
        context = {}
        if req.GET.get('name'):
            context['trainees'] = Trainee.objects.filter(name__icontains=req.GET.get('name'))
        else:
            context['trainees'] = Trainee.objects.all()

        return render(req, 'trainee_list.html', context)

    def post(self, req):
        pass


class AddTrainee(LoginRequiredMixin, views.View):
    def get(self, req):
        context = {'form': TraineeForm()}
        return render(req, 'trainee_add.html', context)

    def post(self, req):
        print("Here!")
        form = TraineeForm(req.POST)

        if form.is_valid():
            trainee = {
                'name': req.POST['name'],
                'birth_date': req.POST['birth_date'],
                'track_id': Track.objects.get(id=req.POST['track_id'])
            }
            Trainee.objects.create(**trainee)
            return HttpResponseRedirect('/trainees')

        context = {'errors': form.errors}
        return render(req, '/trainees/add', context)


@login_required()
def update_trainee(req, id):
    if req.method == 'POST':
        trainee = {
            'name': req.POST['name'],
            'birth_date': req.POST['birth_date'],
            'track_id': Track.objects.get(id=req.POST['track_id'])
        }
        Trainee.objects.filter(id=id).update(**trainee)
        return HttpResponseRedirect('/trainees')

    context = {'trainee': Trainee.objects.get(id=id), 'tracks': Track.objects.all()}
    return render(req, 'trainee_update.html', context)


@login_required()
def delete_trainee(req, id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect('/trainees')
