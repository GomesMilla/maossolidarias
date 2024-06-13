from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CategoriaDoacao(models.Model):
    nome = models.CharField('Nome da categoria', max_length=30)
    resumo = models.CharField('Resumo', max_length=250)
    dataHorarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)

    class Meta:
        verbose_name = "Categoria de doação"
        verbose_name_plural="Categorias de doação"
        app_label = 'base'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class PedirDoacao(models.Model):
    titulo = models.CharField('Assunto', max_length=60)
    slug = models.SlugField('Slug', unique=True, null=True, blank=True)
    fotoImagem = models.ImageField("Imagem de Capa", upload_to="FotoImagemArtigo/")
    tipo = models.ForeignKey("CategoriaDoacao", on_delete=models.CASCADE, related_name="categoria")
    resumo = models.TextField('Informe um resumo do seu pedido')
    descricao = RichTextUploadingField("Descreva tudo que precisa")
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="autor")
    horarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)
    is_active = models.BooleanField(default=False)
    motivo_inativacao = models.TextField('Informe um motivo pelo qual está inativando a solicitação', null=True, blank=True)

    class Meta:
        verbose_name = "Pedir Doacao"
        verbose_name_plural="Pedir Doacao"
        app_label = 'base'
        ordering = ['titulo']

    def __str__(self):
        return str(self.titulo)

class ImagemDoacao(models.Model):
    pedir_doacao = models.ForeignKey('PedirDoacao', on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='photos/')

class VisualizacaoObjeto(models.Model):
    solicitacao = models.ForeignKey("PedirDoacao", on_delete=models.CASCADE, related_name="solicitacao_visualicao")
    ip = models.CharField('Endereço de IP', max_length=250)
    estado = models.CharField('Estado', null=True, blank=True, max_length=60)
    dataHorarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)

    class Meta:
        verbose_name = "Visualização de Solicitação"
        verbose_name_plural="Visualização de Solicitação"
        app_label = 'base'
        ordering = ['solicitacao']

    def __str__(self):
        return self.ip

class ContatarSolicitacao(models.Model):
    solicitacao = models.ForeignKey("PedirDoacao", on_delete=models.CASCADE, related_name="solicitacao_contatar")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_solicitante", blank=True, null=True)
    nome = models.CharField('Nome', max_length=40)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=40, blank=True, null=True)
    assunto = models.CharField('Assunto', max_length=250)
    mensagem = models.TextField('Mensagem')
    dataHorarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)

    class Meta:
        verbose_name = "Contatar Solicitação"
        verbose_name_plural="Contatar Solicitação"
        app_label = 'base'
        ordering = ['assunto']

    def __str__(self):
        return self.assunto


