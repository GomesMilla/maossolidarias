from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CategoriaDoacao(models.Model):
    nome = models.CharField('Nome da categoria', max_length=30)
    resumo = models.CharField('Resumo', max_length=250)
    dataHorarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)


    class Meta:
        verbose_name = "Categoria de doação"
        verbose_name_plural="Categorias de doação"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class PedirDoacao(models.Model):
    titulo = models.CharField('Assunto', max_length=60)
    slug = models.SlugField('Slug', unique=True, null=True, blank=True)
    fotoImagem = models.ImageField("Imagem", upload_to="FotoImagemArtigo/")
    tipo = models.ForeignKey("CategoriaDoacao", on_delete=models.CASCADE, related_name="categoria")
    resumo = models.TextField('Informe um resumo do seu pedido')
    descricao = RichTextUploadingField("Descreva tudo que precisa")
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="autor")
    horarioCriacao = models.DateTimeField('Horário de Criação', auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pedir Doacao"
        verbose_name_plural="Pedir Doacao"
        ordering = ['titulo']

    def __str__(self):
        return str(self.titulo)
