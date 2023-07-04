from django.contrib.messages import constants
from django.core.checks import messages
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from perfil.forms import ContaForm, CategoriaForm
from perfil.models import Conta, Categoria


# Create your views here.
class HomePerfilView(TemplateView):
    template_name = 'perfil/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePerfilView, self).get_context_data(**kwargs)

        context['contas'] = Conta.objects.all()

        context['total_conta'] = Conta.objects.aggregate(models.Sum('valor'))['valor__sum']

        context['categorias'] = Categoria.objects.all()

        return context


class GerenciarView(TemplateView):
    template_name = 'perfil/gerenciar.html'

    def get_context_data(self, **kwargs):
        context = super(GerenciarView, self).get_context_data(**kwargs)

        context['contas'] = Conta.objects.all()

        soma = Conta.objects.aggregate(total_conta=models.Sum('valor'))
        context['total_conta'] = soma['total_conta']

        context['categorias'] = Categoria.objects.all()

        context['forms_conta'] = ContaForm()
        context['forms_categoria'] = CategoriaForm()

        return context

class CadatrarBancoView(CreateView):
    success_url = '/perfil/gerenciar/'
    template_name = 'perfil/gerenciar.html'
    model = Conta
    form_class = ContaForm

class DeletarBancoView(DeleteView):
    model = Conta
    success_url = reverse_lazy('gerenciar')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())

class CadastrarCategoriaView(CreateView):
    success_url = '/perfil/gerenciar/'
    template_name = 'perfil/gerenciar.html'
    model = Conta
    form_class = CategoriaForm

class AtualizarCategoriaView(View):
    model = Categoria
    success_url = reverse_lazy('gerenciar')
    template_name = 'perfil/gerenciar.html'

def atualizarCategoria(request, pk):
    categoria = Categoria.objects.get(pk = pk)
    categoria.essencial = not categoria.essencial
    categoria.save()
    return redirect('gerenciar')