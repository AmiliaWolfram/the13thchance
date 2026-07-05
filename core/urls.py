from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('universities/', views.universities, name='universities'),
    path('employers/', views.employers, name='employers'),
    path('ai-assistant/', views.ai_assistant, name='ai_assistant'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('mentors/', views.mentors, name='mentors'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path("join/", views.join_platform, name="join_platform"),
    path("join/", views.join_platform, name="join_platform"),
    path("student-onboarding/", views.student_onboarding, name="student_onboarding"),
    path("company-onboarding/", views.company_onboarding, name="company_onboarding"),
]