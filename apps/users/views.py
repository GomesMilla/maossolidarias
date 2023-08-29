from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import PessoaJuridicaForm, PessoaFisicaForm
from users.models import User
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from .models import *
from django.utils import timezone
from django.contrib import messages
import logging
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from base.models import PedirDoacao

logger = logging.getLogger(__name__)


class PessoaJuridicaCreateView(CreateView):
    model = User
    form_class = PessoaJuridicaForm
    template_name = 'users/createaccount.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = True        
        return super().form_valid(form)

class PessoaFisicaCreateView(CreateView):
    model = User
    form_class = PessoaFisicaForm
    template_name = 'users/createaccountfisica.html'
    success_url = '/users/login'

    def form_valid(self, form):
        form.instance.is_juridico = False        
        return super().form_valid(form)

class IntroductionView(TemplateView):
    template_name = "presentation/creataccountinitial.html"


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


class PerfilDetailView(DetailView):
    model = User
    template_name = 'users/perfildetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_id = self.kwargs['pk']
        object_user = User.objects.get(pk=object_id)
        list_solicitacoes = PedirDoacao.objects.filter(usuario=object_user)
        
        context['object'] = object_user
        context['list_solicitacoes'] = list_solicitacoes
        
        return context

class PainelAdministrativo(DetailView):
    model = User
    template_name = 'users/painel-administrativo.html'

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


def ViewLogout(request):
    logout(request)
    return redirect('/')