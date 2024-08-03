from django.urls import path

from .views import (
    EmployeesViewSet,
    EngineersView,
    LoginAPI,
    RemoveTokensAPI,
    ClientsViewSet,
    ProjectsViewSet,
    AttachmentsViewSet,
    RequiredAttachmentsViewSet,
    PaymentsViewSet,
    CopyProjectsView,
    DashboardView,
    DelayedProjectsView,
    CommentsViewSet,
    TableViewsViewSet,
    BaladyProjectsViewSet,
    LandSurveyProjectsViewSet,
    SortingDeedsProjectsViewSet,
    GlobalIDsViewSet,
    CopyBaladyProjectsView,
    MoveProjectsViewSet,
    HistoryViewSet,
    GroupsViewSet,
)

from rest_framework.routers import DefaultRouter

from knox import views as knox_views

# from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("design_projects", ProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewsViewSet)
router.register("attachments", AttachmentsViewSet)
router.register("balady_projects", BaladyProjectsViewSet)
router.register("land_survey_projects", LandSurveyProjectsViewSet)
router.register("sorting_deeds_projects", SortingDeedsProjectsViewSet)
router.register("global_ids", GlobalIDsViewSet)
router.register("groups", GroupsViewSet)

urlpatterns = router.urls + [
    # Design Projects
    path("design_projects/copy", CopyProjectsView.as_view(), name="copy_projects"),
    path(
        "design_projects/<int:project_id>/attachments/",
        RequiredAttachmentsViewSet.as_view(),
        name="required_attachments",
    ),
    path(
        "design_projects/<int:project_id>/payments/",
        PaymentsViewSet.as_view(),
        name="payments",
    ),
    path(
        "design_projects/<int:project_id>/history/",
        HistoryViewSet.as_view(),
        name="history",
    ),
    path("move_projects/", MoveProjectsViewSet.as_view(), name="move_projects"),
    path("engineers/", EngineersView.as_view(), name="engineers"),
    # Balady Projects
    path(
        "balady_projects/copy",
        CopyBaladyProjectsView.as_view(),
        name="copy_balady_projects",
    ),
    # Authentication
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path("remove_tokens/", RemoveTokensAPI.as_view(), name="remove_tokens"),
    # path("projects/export", ExportProjectsView.as_view(), name="export_projects"),
    # path("dashboard/", DashboardView.as_view(), name="dashboard"),
    # path("delayed_projects/", DelayedProjectsView.as_view(), name="delayed_projects"),
    # path("hello/", HelloView.as_view(), name="hello"),
    # path("balady_projects/<int:project_id>/payments/", PaymentsViewSet.as_view(), name="payments"),
]
