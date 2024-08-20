from django.urls import path

from .views import (
    EmployeesViewSet,
    EmployeeRolesViewSet,
    EngineersView,
    LoginAPI,
    RemoveTokensAPI,
    ClientsViewSet,
    DesignProjectsViewSet,
    AttachmentsViewSet,
    RequiredAttachmentsViewSet,
    CopyProjectsView,
    CommentsViewSet,
    TableViewsViewSet,
    BaladyProjectsViewSet,
    LandSurveyProjectsViewSet,
    SortingDeedsProjectsViewSet,
    QataryOfficeProjectsViewSet,
    GlobalIDsViewSet,
    CopyBaladyProjectsView,
    MoveProjectsViewSet,
    HistoryViewSet,
    GroupsViewSet,
    PaymentsViewSet,
    RequestSubmissionsView,
    MunicipalityVisitsView,
)

from rest_framework.routers import DefaultRouter

from knox import views as knox_views


router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("design", DesignProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewsViewSet)
router.register("attachments", AttachmentsViewSet)
router.register("balady", BaladyProjectsViewSet)
router.register("land_survey", LandSurveyProjectsViewSet)
router.register("sorting_deeds", SortingDeedsProjectsViewSet)
router.register("global_ids", GlobalIDsViewSet)
router.register("groups", GroupsViewSet)
router.register("qatari", QataryOfficeProjectsViewSet)
# router.register("payments", PaymentsViewSet)

urlpatterns = router.urls + [
    # Design Projects
    path("design/copy", CopyProjectsView.as_view(), name="copy_projects"),
    path(
        "design/<int:project_id>/history/",
        HistoryViewSet.as_view(),
        name="history",
    ),
    path("move_projects/", MoveProjectsViewSet.as_view(), name="move_projects"),
    path("engineers/", EngineersView.as_view(), name="engineers"),
    # Balady Projects
    path(
        "balady/copy",
        CopyBaladyProjectsView.as_view(),
        name="copy_balady_projects",
    ),
    path(
        "balady/<int:project_id>/requests/",
        RequestSubmissionsView.as_view(),
        name="balady_request_submissions",
    ),
    path(
        "balady/<int:project_id>/visits/",
        MunicipalityVisitsView.as_view(),
        name="balady_municipality_visits",
    ),
    
    # common
    path(
        "<str:project_category>/<int:project_id>/attachments/",
        RequiredAttachmentsViewSet.as_view(),
        name="required_attachments",
    ),
    path(
        "<str:project_category>/<int:project_id>/payments/",
        PaymentsViewSet.as_view(),
        name="design_payments",
    ),
    
    # Authentication
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path("remove_tokens/", RemoveTokensAPI.as_view(), name="remove_tokens"),
    path("employee_roles/", EmployeeRolesViewSet.as_view(), name="employee_roles"),
]
