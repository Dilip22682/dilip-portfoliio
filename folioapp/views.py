from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Skill, Project, Experience, Education
from .forms import (
    ProfileForm, SkillForm, ProjectForm,
    ExperienceForm, EducationForm, ContactForm
)


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')
    tools_skills = Skill.objects.filter(category='tools')
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'home.html', {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'tools_skills': tools_skills,
        'experiences': experiences,
        'educations': educations,
        'form': form,
    })


def success(request):
    return render(request, 'contact_success.html')


# ✅ DASHBOARD - protected by login
@login_required(login_url='/dashboard/login/')
def dashboard(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    })


# ✅ PROFILE FORM
@login_required(login_url='/dashboard/login/')
def profile_form(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'dashboard/profile_form.html', {'form': form})


# ✅ SKILL FORM
@login_required(login_url='/dashboard/login/')
def skill_form(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'dashboard/skill_form.html', {'form': form})


@login_required(login_url='/dashboard/login/')
def skill_delete(request, pk):
    Skill.objects.filter(pk=pk).delete()
    return redirect('dashboard')


# ✅ PROJECT FORM
@login_required(login_url='/dashboard/login/')
def project_form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/project_form.html', {'form': form})


@login_required(login_url='/dashboard/login/')
def project_delete(request, pk):
    Project.objects.filter(pk=pk).delete()
    return redirect('dashboard')


# ✅ EXPERIENCE FORM
@login_required(login_url='/dashboard/login/')
def experience_form(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExperienceForm()
    return render(request, 'dashboard/experience_form.html', {'form': form})


@login_required(login_url='/dashboard/login/')
def experience_delete(request, pk):
    Experience.objects.filter(pk=pk).delete()
    return redirect('dashboard')


# ✅ EDUCATION FORM
@login_required(login_url='/dashboard/login/')
def education_form(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EducationForm()
    return render(request, 'dashboard/education_form.html', {'form': form})


@login_required(login_url='/dashboard/login/')
def education_delete(request, pk):
    Education.objects.filter(pk=pk).delete()
    return redirect('dashboard')


# ✅ LOGIN / LOGOUT
from django.contrib.auth import authenticate, login, logout

def dashboard_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')