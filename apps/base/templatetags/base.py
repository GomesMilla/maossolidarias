from django import template
from base.views import get_client_ip
from base.models import VisualizacaoObjeto,PedirDoacao
register = template.Library()


@register.simple_tag()
def registra_acesso_objeto(request, objeto):
    """
    Método que faz estatistica de acesso aos objetos do Vindula
    """
    if not request:
        pass

    else:
        try:
            objetoid = objeto.id
            # slug = objeto.slug
        except AttributeError:
            objetoid = objeto['id']

        try:
            ip = get_client_ip(request)
        except AttributeError:
            ip = request
        else:
            solicitacao = PedirDoacao.objects.get(pk=objetoid)
            visualizacao_analytics = VisualizacaoObjeto(solicitacao=solicitacao, ip=ip)
            visualizacao_analytics.save()

#como eu quero ser reconhecido no mercado de trabalho e como eu vou ser reconhecido por isso
#o que eu vendo
#o que eu quero vender