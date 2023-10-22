from django.urls import path

from portfolio import views
from portfolio.views import HomeView, ContactView, ProjectListView, ProjectDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectListView.as_view(), name="project_list"),
    path("skill/<str:skill_name>/", views.ProjectListView.as_view(), name="portfolio_by_skill"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
]


