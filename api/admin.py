from django.contrib import admin
from .models import Employee, Client, Project, Attachment, Comment, TableView, BaladyProject, LandSurveyProject, SortingDeedsProject

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(TableView)
admin.site.register(BaladyProject)
admin.site.register(LandSurveyProject)
admin.site.register(SortingDeedsProject)