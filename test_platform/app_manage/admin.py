from django.contrib import admin
from app_manage.models import Project

# Register your models here.
# 将model(表)映射到admin管理后台，可以在后台进行操作

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'update_time', 'create_time'] #映射到admin管理后台的字段
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器

admin.site.register(Project, ProjectAdmin)

