from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def students(request):
    return render(request, 'core/students.html')


def universities(request):
    return render(request, 'core/universities.html')


def employers(request):
    return render(request, 'core/employers.html')


def ai_assistant(request):
    return render(request, 'core/ai_assistant.html')


def opportunities(request):
    return render(request, 'core/opportunities.html')


def mentors(request):
    return render(request, 'core/mentors.html')


def how_it_works(request):
    return render(request, 'core/about_us.html')


def join_platform(request):
    return render(request, "core/join_platform.html")


from django.shortcuts import render, redirect

def join_platform(request):
    if request.method == "POST":
        role = request.POST.get("role")

        if role == "student":
            return redirect("core:student_onboarding")

        if role == "company":
            return redirect("core:company_onboarding")

    return render(request, "core/join_platform.html")


def student_onboarding(request):
    return redirect("journey:home")


def company_onboarding(request):
    return render(request, "core/company_onboarding.html")