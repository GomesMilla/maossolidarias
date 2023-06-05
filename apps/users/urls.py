from django.urls import path
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from .views import PessoaJuridicaCreateView, PessoaFisicaCreateView, ViewLogin, PerfilDetailView, ViewLogout

urlpatterns = [
    path("criar-conta/", TemplateView.as_view(template_name="presentation/creataccountinitial.html"), name="criar_conta"),
    path("criar-conta-juridico/", PessoaJuridicaCreateView.as_view(), name="criar_conta_juridico"),
    path("criar-conta-fisico/", PessoaFisicaCreateView.as_view(), name="criar_conta_fisico"),
    path("perfil/<int:pk>", PerfilDetailView.as_view(), name="perfil"),
    path('login/', ViewLogin, name = 'login'),
    path('logout/', ViewLogout, name = 'logout'),

]