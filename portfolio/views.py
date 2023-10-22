from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Project, Skill


# Create your views here.
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()  # Fetch all projects
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        skill_name = self.kwargs.get('skill_name')
        if skill_name:
            return Project.objects.filter(skills__name=skill_name)
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill'] = Skill.objects.all()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'


class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'  # Redirect to a 'thank you' page after sending the mail

    def form_valid(self, form):
        send_mail(
            form.cleaned_data['name'],
            form.cleaned_data['message'],
            form.cleaned_data['email'],
            ['webmaster@example.com'],  # Replace with your email
        )
        return super().form_valid(form)



def portfolio(request, skill_name=None):
    skills = Skill.objects.all()

    if skill_name:
        projects = Project.objects.filter(skills__name=skill_name)
    else:
        projects = Project.objects.all()

    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'skills': skills})


