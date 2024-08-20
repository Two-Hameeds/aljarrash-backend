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
