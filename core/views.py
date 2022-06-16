from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactoForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VDService9:Home'
        # context['url_nuevo'] = 'personas/crear'
        return context

class PresupuestoView(TemplateView):
    template_name = 'presupuesto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VDService9:Presupuesto'
        return context

class ContactoView(FormView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VDService9:Contacto'
        return context