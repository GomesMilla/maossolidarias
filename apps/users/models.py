from django.db import models
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from django.db import IntegrityError
from ckeditor_uploader.fields import RichTextUploadingField
# from djrichtextfield.models import RichTextField



class UserManager(BaseUserManager):
    def get_or_create(self, defaults=None, **kwargs):
        try:
            user = self.get(**kwargs)
            if user.excluido or not user.is_active:
                user.excluido = False
                user.is_active = True
                user.save()
            return user, False
        except self.model.DoesNotExist:
            return self._create_user(**kwargs, defaults=defaults), True

    def _create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Usuário deve ter um email válido")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

    def get_queryset(self):
        return super(UserManager, self).get_queryset().exclude(is_active=False).exclude(excluido=True)

    def todos_usuarios(self):
        return super(UserManager, self).get_queryset()

class Estado(models.Model):
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField(verbose_name="Endereço de E-mail", max_length=255, unique=True, null=True, blank=True)
    imagemperfil = models.ImageField("Foto de Perfil", upload_to="ImagemPerfil/")
    nome_completo = models.CharField(max_length=255, blank=True, null=True)
    # Campos adicionais para pessoa jurídica

    cnpj = models.CharField('CNPJ',max_length=18, blank=True, null=True)
    razao_social = models.CharField('Razão Social',max_length=255, blank=True, null=True)
    is_juridico = models.BooleanField(default=False)
    paginadoperfil = RichTextUploadingField(u'Página do Perfil', default='', blank=True, null=True)
    linkdoperfil = models.CharField(u'Informe um link para redirecionar para a página que desejar.',
                                    default='',
                                    blank=True, null=True,
                                    max_length=240)
    email_extra = models.EmailField(verbose_name="Endereço de E-mail", max_length=255, unique=True, null=True, blank=True)
    telefone_contato =  models.CharField('Telefone',max_length=50, blank=True, null=True)
    telefone_contato_extra =  models.CharField('Telefone Extra',max_length=50, blank=True, null=True)
    cep =  models.CharField("CEP",max_length=50, blank=True, null=True)
    cidade =  models.CharField('Cidade',max_length=50, blank=True, null=True)
    bairro =  models.CharField('Bairro',max_length=50, blank=True, null=True)
    rua =  models.CharField('Rua',max_length=50, blank=True, null=True)
    numero =  models.CharField("Número",max_length=50, blank=True, null=True)
    complemento =  models.CharField("Complemento",max_length=200, blank=True, null=True)


    # Campos adicionais para pessoa física
    cpf = models.CharField(max_length=14, blank=True, null=True)  


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    excluido = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        if not self.pk:
            usuarios_qs = User.objects.todos_usuarios().filter(Q(excluido=True) | Q(is_active=False), username=self.username)
            if usuarios_qs:
                usuarios_qs.update(is_active=True, excluido=False)
                user = usuarios_qs.first()
                return usuarios_qs.first()

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        inativar = kwargs.get("inativar", False)
        if not inativar:
            self.excluido = True
        self.is_active = False
        self.save()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

class ProfileManager(BaseUserManager):
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset().exclude(user__is_active=False).exclude(user__excluido=True)

    def todos_usuarios(self):
        return super(ProfileManager, self).get_queryset()

    def usuarios_inativos(self):
        return super(ProfileManager, self).get_queryset().filter(user__is_active=False)

    def usuarios_ativos(self):
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class DenunciarEmpresa(models.Model):    
    denunciante = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_denunciante", blank=True, null=True)
    denunciado = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_denunciado", blank=True, null=True)
    nome = models.CharField('Nome', max_length=40)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=40, blank=True, null=True)
    assunto = models.CharField('Assunto', max_length=250)
    mensagem = models.TextField('Descreva o motivo da denúncia')
    dataHorarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)

    class Meta:
        verbose_name = "Denuncia Empresa"
        verbose_name_plural="Denuncias Empresa"
        app_label = 'users'
        ordering = ['assunto']

    def __str__(self):
        return self.assunto