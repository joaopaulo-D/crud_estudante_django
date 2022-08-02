from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Estudante

class EstudanteList(ListView):
    model = Estudante

class EstudanteDetail(DetailView):
    model = Estudante

class EstudanteCreate(CreateView):
    model = Estudante
    fields = ['nome', 'matricula', 'curso']
    success_url = reverse_lazy('estudante_list')

class EstudanteUpdate(UpdateView):
    model = Estudante
    fields = ['nome', 'matricula', 'curso']
    success_url = reverse_lazy('estudante_list')

class EstudanteDelete(DeleteView):
    model = Estudante
    success_url = reverse_lazy('estudante_list')