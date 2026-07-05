from django.urls import path
from . import views

app_name = "journey"

urlpatterns = [
    path("", views.journey_home, name="home"),
    path("profile/", views.profile_step, name="profile"),
    path("ai-analysis/", views.ai_analysis, name="ai_analysis"),
    path("roadmap/", views.roadmap, name="roadmap"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("career-score/", views.career_score, name="career_score"),
    path("interview/", views.interview, name="interview"),
    path("networking/", views.networking, name="networking"),
    path("jobs/", views.jobs, name="jobs"),
]