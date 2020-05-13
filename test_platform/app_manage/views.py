from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_manage.models import Project
from app_manage.forms import ProjectForm

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


# def mange(requset):
#     pass
#     # return render(requset)