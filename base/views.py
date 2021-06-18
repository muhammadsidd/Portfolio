from django.shortcuts import render, redirect
from .models import Project, Skill, Message
from .forms import ProjectForm
# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body ='')
    skills = Skill.objects.filter(body ='')
    context = {'projects':projects, 'skills':skills, 'detailedSkills':detailedSkills}
    return render(request, 'base/home.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id = pk)
    context = {'project':project}
    return render(request, 'base/project.html', context)

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/project_form.html',context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)

    if request.method == 'POST': 
        # need to pass instance = project to let tDjango know which project needs to be updated,
        # if we dont pass instance = project, new project will be created. 
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/project_form.html',context)

def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read') #messages that arent read top priority. for reverse use '-is_read'
    context = {'inbox':inbox}
    return render(request, 'base/inbox.html',context)