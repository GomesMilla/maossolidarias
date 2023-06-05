from django import forms
from .models import CategoriaDoacao, PedirDoacao

class PedirDoacaoForm(forms.ModelForm):

    class Meta:
        model = PedirDoacao
        exclude = ('slug', 'horarioCriacao', 'is_active', 'usuario')