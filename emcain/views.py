from django.shortcuts import render
from .models import *

nav = {'home': '/', 'portfolio': '/projects', 'contact': '/contact'}

# Main page
def index(request):
    skills = Skill.objects.all()
    return render(request, 'index.html', context={'skills' : skills, 'nav': nav, 'title': 'Home'})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', context={'nav': nav, 'projects': projects, 'title': 'Portfolio'})

def project(request, project_id):
    proj = Project.objects.get(id=project_id)
    imgs = ProjectImage.objects.filter(project=proj)
    return render(request, 'project.html', context={'nav': nav, 'proj': proj, 'title': proj.name, 'imgs': imgs})
