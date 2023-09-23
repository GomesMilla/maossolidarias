from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('login/', ViewLogin, name = 'login'),
    path('logout/', ViewLogout, name = 'logout'),
    path("criar-conta/", TemplateView.as_view(template_name="presentation/creataccountinitial.html"), name="criar_conta"),
    
    # Jurídico
    path("criar-conta-juridico/", PessoaJuridicaCreateView.as_view(), name="criar_conta_juridico"),
    path("conta-juridico/<int:pk>/edit", PessoaJuridicaUpdateView.as_view(), name="atualizar_conta_juridico"),
    path("perfil/<int:pk>/juridica", login_required(PerfilDetailView.as_view()), name="perfil"),
    path("painel-administrativo/<int:pk>", PainelAdministrativo.as_view(), name="painel_administrativo"),
    
    # Físico
    path("criar-conta-fisico/", PessoaFisicaCreateView.as_view(), name="criar_conta_fisico"),
    path("conta-fisica/<int:pk>/edit", login_required(PessoaFisicaUpdateView.as_view()), name="atualizar_conta_fisica"),
    path("perfil/<int:pk>/fisica", PerfilDetailFisicaView.as_view(), name="perfil_pessoa_fisica"),

    path('Ajax-Verificar-Email/', AjaxVerificarEmail, name="AjaxVerificarEmail"),
]
