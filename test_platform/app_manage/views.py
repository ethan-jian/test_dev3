from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app_manage.models import Project

# Create your views here.


@login_required
def mange(request):
    """
    项目管理
    """
    project_list = Project.objects.all()
    return render(request, 'manage.html', {'projects': project_list})


def add_project(request):
    """
    新增项目
    """
    return render(request, 'project_add.html',)


# def mange(requset):
#     pass
#     # return render(requset)