from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Instructor


# Create your views here.
@login_required()
def list_instructors(req):
    instructors = Instructor.objects.all()
    return render(req, 'instructor_list.html', {'instructors': instructors})


@login_required()
def add_instructor(req):
    context = {'messages': []}
    if req.method == 'POST':
        instructor = {}

        if req.POST['name'] is not None:
            instructor['name'] = req.POST['name']
        else:
            context['messages'].append('Name must be entered!')

        if req.POST['salary'] is not None:
            instructor['salary'] = int(req.POST['salary'])
        else:
            context['messages'].append('Salary must be entered!')
        if req.POST['birth_date'] is not None:
            instructor['birth_date'] = req.POST['birth_date']
        else:
            context['messages'].append('Birth date must be entered!')

        if len(context['messages']) > 0:
            return render(req, 'instructor_add.html', context)
        else:
            Instructor.objects.create(**instructor)
            return HttpResponseRedirect('/instructors')

    return render(req, 'instructor_add.html', context)


@login_required()
def update_instructor(req):
    return render(req, 'trainers.html', {})


@login_required()
def delete_instructor(req, id):
    Instructor.objects.filter(id=id).delete()
    return HttpResponseRedirect('/instructors')
