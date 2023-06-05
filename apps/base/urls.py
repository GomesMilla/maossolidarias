from django.urls import path
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from .views import PedirDoacaoCreateView, SolicitacoesListView, SolicitacaoDetailView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("objetivo/", TemplateView.as_view(template_name="presentation/objetivo.html"), name="objetivo"),
    path("introducao/", TemplateView.as_view(template_name="presentation/introduction.html"), name="introducao"),
    path("pedir-doacao/", login_required(PedirDoacaoCreateView.as_view()), name="pedir_doacao"),
    path("solicitacoes/", SolicitacoesListView.as_view(), name="solicitacoes"),
    path("ver-solicitacao/<int:pk>", SolicitacaoDetailView.as_view(), name="ver_solicitacao"),
]
