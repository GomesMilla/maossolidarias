from django import template

from base.models import PedirDoacao, VisualizacaoObjeto
from base.views import get_client_ip, get_state_from_ip

register = template.Library()
from users.models import User


@register.simple_tag()
def registra_acesso_objeto(request, objeto):

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
            state = get_state_from_ip(ip)
            try:
                visualizacao_analytics = VisualizacaoObjeto.objects.get(solicitacao=solicitacao, estado=state)
                # Atualizar o objeto existente, se necessário
                # visualizacao_analytics.algum_campo = algum_valor
                visualizacao_analytics.save()
            except VisualizacaoObjeto.DoesNotExist:
                visualizacao_analytics = VisualizacaoObjeto(solicitacao=solicitacao, ip=ip, estado=state)
                visualizacao_analytics.save()



@register.simple_tag()
def verifica_quantidade_de_solicitacoes(instituicao_id):

    user = User.objects.get(pk=instituicao_id)
    doacoes = PedirDoacao.objects.filter(usuario=user)
    quantidade = doacoes.count()
    return quantidade

#como eu quero ser reconhecido no mercado de trabalho e como eu vou ser reconhecido por isso
#o que eu vendo
#o que eu quero vender
