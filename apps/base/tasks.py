from celery import shared_task
from .models import (CategoriaDoacao, ContatarSolicitacao, PedirDoacao,
                    VisualizacaoObjeto)

@shared_task
def listagem_de_solicitacoes():
    listcategoria = CategoriaDoacao.objects.all()
    dictcategoria = {}
    listafina = []
    for categoria in listcategoria:
        listdoacao = PedirDoacao.objects.filter(tipo=categoria).values_list('titulo', flat=True)
        dictcategoria ={
            "category": categoria.nome,
            "listdoacao": list(listdoacao),
        }
        listafina.append(dictcategoria)
    return listafina