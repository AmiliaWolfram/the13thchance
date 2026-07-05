from django.shortcuts import render


def journey_home(request):
    return render(request, "journey/home.html")


def profile_step(request):
    return render(request, "journey/profile.html")


def ai_analysis(request):
    return render(request, "journey/ai_analysis.html")


def roadmap(request):
    return render(request, "journey/roadmap.html")


def skills(request):
    return render(request, "journey/skills.html")


def projects(request):
    return render(request, "journey/projects.html")


def portfolio(request):
    return render(request, "journey/portfolio.html")


def career_score(request):
    return render(request, "journey/career_score.html")


def interview(request):
    return render(request, "journey/interview.html")


def networking(request):
    return render(request, "journey/networking.html")


def jobs(request):
    return render(request, "journey/jobs.html")