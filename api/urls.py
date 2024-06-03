from django.urls import path

from .views import EmployeesViewSet, RegisterAPI, LoginAPI, ClientsViewSet, ProjectsViewSet, CopyProjectsView, DashboardView, DelayedProjectsView, CommentsViewSet, TableViewsViewSet, HelloView

from rest_framework.routers import DefaultRouter

from knox import views as knox_views
# from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("projects", ProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewsViewSet)

urlpatterns = router.urls + [
    path("projects/copy", CopyProjectsView.as_view(), name="copy_projects"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("delayed_projects/", DelayedProjectsView.as_view(), name="delayed_projects"),
    path("hello/", HelloView.as_view(), name="hello"),
    # path("auth/", obtain_auth_token, name="api_token_auth"),
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('logout/', knox_views.LogoutView.as_view(), name="logout"),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name="logoutall"),
]