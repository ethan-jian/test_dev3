from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_manage.models import Project
from app_manage.forms import ProjectForm, ProjectEditForm

# Create your views here.

@login_required
def mange(request):
    """
    项目管理
    """
    project_list = Project.objects.all()
    return render(request, 'project_list.html', {'projects': project_list})


def add_project(request):
    """
    新增项目
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)

        return HttpResponseRedirect('/project/')
    else:
        form = ProjectForm()

    return render(request, 'project_add.html', {'form': form})


def edit_project(request, pid):
    """编辑项目"""
    if request.method == 'POST': #更新项目
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()

        return HttpResponseRedirect('/project/')

    else:
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()

        return render(request, 'project_edit.html', {
            'form': form, 'id': pid})
