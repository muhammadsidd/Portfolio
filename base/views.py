from django.shortcuts import render
from .models import Project, Tag, Skill
# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'base/home.html', {'projects':projects, 'skills':skills})