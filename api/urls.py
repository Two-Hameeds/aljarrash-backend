from django.urls import path

from .views import (
    EmployeesViewSet,
    EngineersView,
    RegisterAPI,
    LoginAPI,
    RemoveTokensAPI,
    ClientsViewSet,
    ProjectsViewSet,
    ExportProjectsView,
    AttachmentsViewSet,
    CopyProjectsView,
    DashboardView,
    DelayedProjectsView,
    CommentsViewSet,
    TableViewsViewSet,
    BaladyProjectsViewSet,
    LandSurveyProjectsViewSet,
    SortingDeedsProjectsViewSet,
    CopyBaladyProjectsView,
    HelloView,
)

from rest_framework.routers import DefaultRouter

from knox import views as knox_views

# from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("projects", ProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewsViewSet)
router.register("attachments", AttachmentsViewSet)
router.register("balady_projects", BaladyProjectsViewSet)
router.register("land_survey_projects", LandSurveyProjectsViewSet)
router.register("sorting_deeds_projects", SortingDeedsProjectsViewSet)

urlpatterns = router.urls + [
    path("projects/copy", CopyProjectsView.as_view(), name="copy_projects"),
    path("projects/export", ExportProjectsView.as_view(), name="export_projects"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("delayed_projects/", DelayedProjectsView.as_view(), name="delayed_projects"),
    path("hello/", HelloView.as_view(), name="hello"),
    path("engineers/", EngineersView.as_view(), name="engineers"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path("remove_tokens/", RemoveTokensAPI.as_view(), name="remove_tokens"),
    path(
        "balady_projects/copy",
        CopyBaladyProjectsView.as_view(),
        name="copy_balady_projects",
    ),
]
