from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import PedirDoacao, CategoriaDoacao, VisualizacaoObjeto
from .forms import PedirDoacaoForm
from users.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.views import LogoutView
from dateutil.relativedelta import relativedelta
from django.db.models import Count
import requests
import datetime
import calendar

from datetime import date
class GoalView(TemplateView):
    template_name = "presentation/objetivo.html"

class IntroductionView(ListView):
    model = PedirDoacao
    template_name = "presentation/introduction.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()

        visualizacoes_por_solicitacao = VisualizacaoObjeto.objects.values('solicitacao').annotate(
            total_visualizacoes=Count('solicitacao')
        ).order_by('-total_visualizacoes')[:3]
  
        # Obtenha as solicitações correspondentes às visualizações mais acessadas
        solicitacoes_mais_acessadas = PedirDoacao.objects.filter(
            pk__in=[item['solicitacao'] for item in visualizacoes_por_solicitacao]
        )
        context['list_solicitacoes'] = PedirDoacao.objects.filter(is_active=True) 
        context['solicitacoes_mais_acessadas'] = solicitacoes_mais_acessadas
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
        return context

class SolicitacaoDetailView(DetailView):
    model = PedirDoacao
    template_name = 'doacao/solicitacaodetail.html'

class RelatoriosView(DetailView):
    model = PedirDoacao
    template_name = 'users/relatorios.html'

    def get_context_data(self, **kwargs):
        context = super(RelatoriosView, self).get_context_data(**kwargs)
        solicitacao = PedirDoacao.objects.get(pk=self.kwargs.get('pk'))
        all_acessos = VisualizacaoObjeto.objects.filter(solicitacao=solicitacao)
        unique_ips = set(item.ip for item in all_acessos)

        all_acessos_mes = VisualizacaoObjeto.objects.filter(solicitacao=solicitacao, dataHorarioCriacao__month=date.today().month, dataHorarioCriacao__year=date.today().year)
        unique_ips_mes = set(item.ip for item in all_acessos_mes)

        hoje = datetime.datetime.today()
        mesatual = hoje.month
        anoatual = hoje.year
        ultimodia = calendar.monthrange(anoatual, mesatual)[1]
        inicio_do_mes = hoje.replace(day=1)
        final_do_mes = inicio_do_mes + relativedelta(months=1, days=-1)
        dias_do_mes_atual = [datetime.date(anoatual, mesatual, dia) for dia in range(1, ultimodia + 1)]
        lista_dias_do_mes_atual = [dia.day for dia in dias_do_mes_atual]

        lista_dias_visitas = []
        for dia in dias_do_mes_atual:
            qs_mes_loop = all_acessos_mes.filter(dataHorarioCriacao__date=dia)
            totalacessoloop = qs_mes_loop.count()
            lista_dias_visitas.append(totalacessoloop)

        dict_meses = {}
        for mes in [1, 2, 3, 4, 5, 6]:
            mes_do_loop = datetime.datetime.now() - relativedelta(months=mes)
            inicio_mes_do_loop = mes_do_loop.replace(day=1)
            final_mes_do_loop = inicio_mes_do_loop + relativedelta(months=1, days=-1)
            qs_mes_loop = all_acessos.filter(dataHorarioCriacao__gte=inicio_mes_do_loop, dataHorarioCriacao__lte=final_mes_do_loop)
            totaldeacessos_mes_loop = qs_mes_loop.count()
            dict_meses["mes" + str(mes)] = mes_do_loop.strftime("%B")
            dict_meses["mes" + str(mes) + "acessos"] = totaldeacessos_mes_loop
        
        context['qtd_list_acessos_total'] = len(all_acessos)
        context['qtd_list_acessos_total_unicos'] = len(unique_ips)
        context['qtd_list_acessos_mes_total'] = len(all_acessos_mes)
        context['qtd_list_acessos_mes_unico'] = len(unique_ips_mes)
        context['lista_dias_visitas'] = lista_dias_visitas
        context['dias_do_mes_atual'] = lista_dias_do_mes_atual
        context['dict_meses'] = dict_meses
        context['ultimosacessos'] = VisualizacaoObjeto.objects.filter(solicitacao=solicitacao).order_by('-dataHorarioCriacao')[:10]
        

        return context

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_state_from_ip(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    state = data.get('region') 
    return state
