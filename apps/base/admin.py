from django.contrib import admin
from .models import CategoriaDoacao, PedirDoacao, VisualizacaoObjeto, ContatarSolicitacao

admin.site.register(CategoriaDoacao)
admin.site.register(PedirDoacao)
admin.site.register(VisualizacaoObjeto)
admin.site.register(ContatarSolicitacao)
