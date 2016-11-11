from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template

from random import choice

from .forms import ContactForm
from .helpers import recaptcha_verify
from .models import *

nav = {'home': '/', 'portfolio': '/projects', 'contact': '/contact'}

# Main page
def index(request):
    skills = Skill.objects.all()
    return render(request, 'index.html', context={'skills' : skills, 'nav': nav, 'title': 'Home'})

# list all projects
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', context={'nav': nav, 'projects': projects, 'title': 'Portfolio'})

# details on a particular project
def project(request, project_id):
    proj = Project.objects.get(id=project_id)
    imgs = ProjectImage.objects.filter(project=proj)
    return render(request, 'project.html', context={'nav': nav, 'proj': proj, 'title': proj.name, 'imgs': imgs})

# contact form
def contact(request):
    form_class = ContactForm
    form = form_class()

    phrases = ['make it so', 'engage', 'energize']
    submit_phrase = choice(phrases)

    errors = {}

    if request.method == 'POST':
        data = request.POST
        rcverify = recaptcha_verify(request)

        form = form_class(data=data, captcha_valid=rcverify)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')

            contact_email = request.POST.get('contact_email', '')

            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })

            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website' + '',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/contact')
        else:
            print(form.errors)
            errors = form.errors


    return render(request, 'contact.html', context={'form': form, 'nav': nav, 'title': 'Contact Me', 'submit_phrase': submit_phrase, 'recaptcha_key': settings.RECAPTCHA_PUBLIC_KEY})