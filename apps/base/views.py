from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import PedirDoacao, CategoriaDoacao
from .forms import PedirDoacaoForm
from users.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.views import LogoutView


class GoalView(TemplateView):
    template_name = "presentation/objetivo.html"

class IntroductionView(ListView):
    model = PedirDoacao
    template_name = "presentation/introduction.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context['list_solicitacoes'] = PedirDoacao.objects.filter(is_active=True)
        return context

class PedirDoacaoCreateView(CreateView):
    model = PedirDoacao
    form_class = PedirDoacaoForm
    template_name = 'doacao/pedirdoacao.html'
    success_url = '/base/objetivo'

    def form_valid(self, form):
        user = self.request.user
        objuser = User.objects.get(pk=user.id)    
        form.instance.usuario = user
        form.instance.is_active = True          
        return super().form_valid(form)

class PedirDoacaolUpdate(UpdateView):
    form_class = PedirDoacaoForm
    model = PedirDoacao
    template_name = 'doacao/pedirdoacao.html'
    success_url = reverse_lazy('solicitacoes')

    def form_valid(self, form):
        user = self.request.user
        objuser = User.objects.get(pk=user.id)    
        form.instance.usuario = user
        form.instance.is_active = True          
        return super().form_valid(form)

class SolicitacoesListView(ListView):
    model = PedirDoacao
    template_name = 'doacao/list_solicitacoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context['list_solicitacoes'] = PedirDoacao.objects.filter(is_active=True)
        context['list_categorias'] = CategoriaDoacao.objects.all()
        return context

class SolicitacoesPorCategoria(DetailView):
    model = CategoriaDoacao
    template_name = 'doacao/list_solicitacoes.html'

    def get_context_data(self, **kwargs):
        context = super(SolicitacoesPorCategoria, self).get_context_data(**kwargs)
        categoria = CategoriaDoacao.objects.get(pk=self.kwargs.get('pk'))
        context['list_solicitacoes'] = PedirDoacao.objects.filter(is_active=True, tipo=categoria)
        context['list_categorias'] = CategoriaDoacao.objects.all()
        context['locategoriaja'] = categoria
        ip = get_client_ip(self.request)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(ip)
        user_ip = self.request.META.get('REMOTE_ADDR')
        print(user_ip)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return context

class SolicitacaoDetailView(DetailView):
    model = PedirDoacao
    template_name = 'doacao/solicitacaodetail.html'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip