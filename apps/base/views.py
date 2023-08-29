from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import PedirDoacao
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

# class ArticleDetailView(DetailView):
#     model = Article

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["now"] = timezone.now()
#         return context


class SolicitacoesListView(ListView):
    model = PedirDoacao
    template_name = 'doacao/list_solicitacoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context['list_solicitacoes'] = PedirDoacao.objects.filter(is_active=True)
        return context

class SolicitacaoDetailView(DetailView):
    model = PedirDoacao
    template_name = 'doacao/solicitacaodetail.html'