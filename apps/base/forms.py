from django import forms
from .models import CategoriaDoacao, PedirDoacao, ContatarSolicitacao

class PedirDoacaoForm(forms.ModelForm):

    class Meta:
        model = PedirDoacao
        exclude = ('slug', 'horarioCriacao', 'is_active', 'usuario', 'motivo_inativacao')

class ContatarSolicitacaoForm(forms.ModelForm):

    class Meta:
        model = ContatarSolicitacao
        exclude = ('user', 'dataHorarioCriacao')