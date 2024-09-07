from django.contrib import admin
from .models import (
    Employee,
    Client,
    DesignProject,
    Attachment,
    Comment,
    TableView,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    QatariOfficeProject,
)

from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
import os


# Register your models here.
admin.site.register(DesignProject)
admin.site.register(BaladyProject)
admin.site.register(LandSurveyProject)
admin.site.register(SortingDeedsProject)
admin.site.register(QatariOfficeProject)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(TableView)


class LogAdminView(admin.ModelAdmin):
    change_list_template = "admin/view_log.html"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view_log/', self.admin_site.admin_view(self.view_log), name='view-log')
        ]
        
        return custom_urls + urls
    
    def view_log(self, request):
        log_file_path = os.path.join(os.path.dirname(__file__), '..', 'debuggers/debug.log')
        
        try:
            with open(log_file_path, 'r') as f:
                log_content = f.read()
        except FileNotFoundError:
            log_content = "Log file not found."
            
            
        context = {
            'log_content': log_content,
            'title': 'Log File Content',
        }
        return TemplateResponse(request, 'admin/view_log.html', context)