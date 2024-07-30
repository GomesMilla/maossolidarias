from django import forms

from .models import CategoriaDoacao, ContatarSolicitacao, PedirDoacao, ImagemDoacao


class PedirDoacaoForm(forms.ModelForm):
    # imagens = forms.FileField(
    #     widget=forms.ClearableFileInput(attrs={
    #         "multiple": True,
    #     }),
    #     label="",
    #     required=False
    # )

    class Meta:
        model = PedirDoacao
        exclude = ('slug', 'horarioCriacao', 'is_active', 'usuario', 'motivo_inativacao')

    def save(self, commit=True):
        instance = super(PedirDoacaoForm, self).save(commit=commit)
        if 'imagens' in self.files:
            for image in self.files.getlist('imagens'):
                ImagemDoacao.objects.create(pedir_doacao=instance, imagem=image)
        return instance

class ContatarSolicitacaoForm(forms.ModelForm):

    class Meta:
        model = ContatarSolicitacao
        exclude = ('user', 'dataHorarioCriacao')
