import logging
import re
import unicodedata

from base.models import CategoriaDoacao, PedirDoacao, VisualizacaoObjeto
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, redirect, render
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.views.generic.detail import DetailView

from users.forms import PessoaFisicaForm, PessoaJuridicaForm
from users.models import User

from .forms import *
from .models import *

logger = logging.getLogger(__name__)

def ViewLogin(request):
    if request.user.is_authenticated:
        return redirect('solicitacoes')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('solicitacoes')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            logger.error('Falha na autenticação do usuário')

    context = {
        "nomePagina": "MarkCross"
    }
    return render(request, 'users/login.html', context)


def ViewLogout(request):
    logout(request)
    return redirect('/')

class PessoaJuridicaCreateView(CreateView):
    model = User
    form_class = PessoaJuridicaForm
    template_name = 'users/juridico/createaccount.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = True        
        return super().form_valid(form)

class PessoaJuridicaUpdateView(UpdateView):
    model = User
    form_class = PessoaJuridicaEditarForm
    template_name = 'users/juridico/atualizar-conta-juridico.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = True        
        return super().form_valid(form)


class PessoaFisicaCreateView(CreateView):
    model = User
    form_class = PessoaFisicaForm
    template_name = 'users/fisica/createaccountfisica.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = False        
        return super().form_valid(form)

class PessoaFisicaUpdateView(UpdateView):
    model = User
    form_class = PessoaFisicaEditarForm
    template_name = 'users/fisica/atualizar-conta-fisica.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = False        
        return super().form_valid(form)

class PerfilDetailView(DetailView):
    model = User
    template_name = 'users/juridico/perfildetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_id = self.kwargs['pk']
        object_user = User.objects.get(pk=object_id)
        list_solicitacoes = PedirDoacao.objects.filter(usuario=object_user)
        
        context['object'] = object_user
        context['list_solicitacoes'] = list_solicitacoes
        
        return context

class PerfilDetailView(DetailView):
    model = User
    template_name = 'users/juridico/perfildetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_id = self.kwargs['pk']
        object_user = User.objects.get(pk=object_id)
        list_solicitacoes = PedirDoacao.objects.filter(usuario=object_user, is_active=True)
        context['list_solicitacoes'] = list_solicitacoes
        context['object'] = object_user
        
        return context

class PerfilDetailFisicaView(DetailView):
    model = User
    template_name = 'users/fisica/perfildetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_id = self.kwargs['pk']
        object_user = User.objects.get(pk=object_id)
        visualizacoes_por_solicitacao = VisualizacaoObjeto.objects.values('solicitacao').annotate(
            total_visualizacoes=Count('solicitacao')
        ).order_by('-total_visualizacoes')[:3]

        # Obtenha as solicitações correspondentes às visualizações mais acessadas
        solicitacoes_mais_acessadas = PedirDoacao.objects.filter(
            pk__in=[item['solicitacao'] for item in visualizacoes_por_solicitacao]
        )
        context['solicitacoes_mais_acessadas'] = solicitacoes_mais_acessadas
        context['object'] = object_user
        
        return context

class PainelAdministrativo(DetailView):
    model = User
    template_name = 'users/juridico/painel-administrativo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_id = self.kwargs['pk']
        object_user = User.objects.get(pk=object_id)
        list_solicitacoes = PedirDoacao.objects.filter(usuario=object_user)
        list_solicitacoes_abertas = PedirDoacao.objects.filter(usuario=object_user, is_active=True)
        list_solicitacoes_inativas = PedirDoacao.objects.filter(usuario=object_user, is_active=False)
        
        context['object'] = object_user
        context['list_solicitacoes'] = list_solicitacoes
        context['list_solicitacoes_abertas'] = list_solicitacoes_abertas
        context['list_solicitacoes_inativas'] = list_solicitacoes_inativas
        context['qtd_list_solicitacoes'] = list_solicitacoes.count()
        context['qtd_list_solicitacoes_abertas'] = list_solicitacoes_abertas.count()
        context['qtd_list_solicitacoes_inativas'] = list_solicitacoes_inativas.count()        
        return context

def AjaxVerificarEmail(request):
    email = request.GET.get('Email', None)
        
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    if not data['is_taken']:
        data['error_message'] = 'E-mail não cadastrado!'

    return JsonResponse(data)

class InstituicoesListView(ListView):
    model = User
    template_name = 'users/juridico/lista-intituicoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instituicoes = User.objects.all()
        cidades_unicas = tranformar_cidades_unicas(instituicoes)
        context['instituicoes'] = User.objects.filter(is_juridico=True, is_active=True)
        context['cidades_unicas'] = cidades_unicas
        return context

def tranformar_cidades_unicas(instituicoes):
    cidades_unicas = set()
    for instituicao in instituicoes:
        cidade = instituicao.cidade            
        if cidade is not None:
            cidade_normalizada = unicodedata.normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('utf-8')
            cidade_normalizada = cidade_normalizada.lower()                
            cidades_unicas.add(cidade_normalizada)
    return cidades_unicas

class ListarInstituicoesPorCidadeView(ListView):
    model = User
    template_name = 'users/juridico/lista-intituicoes.html'
    context_object_name = 'instituicoes'

    def get_context_data(self, **kwargs):
        context = super(ListarInstituicoesPorCidadeView, self).get_context_data(**kwargs)
        cidade = self.kwargs['cidade'] 
        instituicoes = User.objects.all()
        cidades_unicas = tranformar_cidades_unicas(instituicoes)
        instituicoes = get_list_or_404(User, cidade__icontains=cidade)
        context['instituicoes'] = instituicoes
        context['cidades_unicas'] = cidades_unicas
        context['cidadev'] = cidade
        return context
