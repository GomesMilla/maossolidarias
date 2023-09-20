from django import forms
from .models import CategoriaDoacao, PedirDoacao, ContatarSolicitacao

class PedirDoacaoForm(forms.ModelForm):

    class Meta:
        model = PedirDoacao
        exclude = ('slug', 'horarioCriacao', 'is_active', 'usuario', 'motivo_inativacao')

class ContatarSolicitacaoForm(forms.Form):

    class Meta:
        model = ContatarSolicitacao
        fields = ('__all__')