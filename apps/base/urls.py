from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path("pedir-doacao/", login_required(PedirDoacaoCreateView.as_view()), name="pedir_doacao"),
    path("lista-doacoes/", login_required(ListagemSolicitacoes.as_view()), name="lista_doacoes"),
    path("solicitacoes/", SolicitacoesListView.as_view(), name="solicitacoes"),
    path("solicitacoes-por-categoria/<int:pk>", SolicitacoesPorCategoria.as_view(), name="solicitacoes_por_categoria"),
    path("solicitacao/<int:pk>/edit", login_required(PedirDoacaolUpdate.as_view()), name="editar_solicitacao"),
    path("ver-solicitacao/<int:pk>", SolicitacaoDetailView.as_view(), name="ver_solicitacao"),
    path("inativar-solicitacao/<int:pk>", login_required(DesativarSolicitacao.as_view()), name="inativar_solicitacao"),
    path("relatorios/<int:pk>", login_required(RelatoriosView.as_view()), name="relatorios"),
    path("contatos/<int:pk>", login_required(ContatosSolicitacaoView.as_view()), name="contatos"),

]
