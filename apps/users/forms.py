from django import forms

from users.models import User, DenunciarEmpresa
from users.utils import validate_username
from django.core.exceptions import ValidationError

class PessoaJuridicaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()

    def save(self, commit=True):
        user = super(PessoaJuridicaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'nome_completo', 'cnpj', 'razao_social', 'imagemperfil', 'telefone_contato', 
        'cep','cidade' ,'bairro', 'rua', 'numero', 'complemento', 'password']

class PessoaJuridicaEditarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'nome_completo', 'cnpj', 'razao_social', 'imagemperfil', 'email_extra', 'telefone_contato', 'telefone_contato_extra', 
        'cep','cidade' ,'bairro', 'rua', 'numero', 'complemento', 'paginadoperfil', 'linkdoperfil']

    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username

class PessoaFisicaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(validators=[validate_username])

    def save(self, commit=True):
        user = super(PessoaFisicaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username
    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'email', 'imagemperfil', 'password']

class PessoaFisicaEditarForm(forms.ModelForm):
    username = forms.CharField(validators=[validate_username])
    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'email', 'imagemperfil', 'email', 'email_extra', 'telefone_contato','telefone_contato_extra','paginadoperfil', 'linkdoperfil']

    def clean_username(self):
        username = self.cleaned_data['username']
        validate_username(username)
        return username

class DenunciarEmpresaForm(forms.ModelForm):

    class Meta:
        model = DenunciarEmpresa
        exclude = ['dataHorarioCriacao']