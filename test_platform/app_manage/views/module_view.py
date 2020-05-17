from app_manage.models import Module
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_manage.models import Project
from app_manage.forms import ModuleForm


def list_module(request):
    """模块管理"""

    module_list = Module.objects.all()
    return render(request, 'module/list.html', {
        "modules": module_list})

def add_module(request):
    """新增模块"""
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Module.objects.create(name=name, describe=describe, project=project)

        return HttpResponseRedirect('/manage/module_list/')
    else:
        form = ModuleForm()

    return render(request, 'module/add.html', {'form': form})

def edit_module(request, mid):
    """编辑模块"""
    if request.method == 'POST': #更新模块
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = form.cleaned_data['project']
            describe = form.cleaned_data['describe']
            p = Module.objects.get(id=mid)
            p.project = project
            p.name = name
            p.describe = describe
            p.save()

        return HttpResponseRedirect('/manage/module_list/')

    else:
        if mid:
            m = Module.objects.get(id=mid)
            form = ModuleForm(instance=m)
        else:
            form = ModuleForm()

        return render(request, 'module/edit.html', {
            'form': form, 'id': mid})


def delete_module(request, mid):
    """删除模块"""
    if request.method == 'GET':
        p = Module.objects.get(id=mid)
        p.delete()

        return HttpResponseRedirect('/manage/module_list/')
    else:
        return HttpResponseRedirect('/manage/module_list/')