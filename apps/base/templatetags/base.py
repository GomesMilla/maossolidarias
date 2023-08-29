from django import template

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
            classname = objeto.class_name()
        except AttributeError:
            # trata contedo via cache
            if objeto['tipodepost']:
                classname = 'PostModel'

        try:
            objetoid = objeto.id
            # slug = objeto.slug
        except AttributeError:
            objetoid = objeto['id']

        try:
            owner = request.user
        except AttributeError:
            owner = request

        if owner.is_anonymous:
            pass
        else:
            model = eval(classname)._meta.model_name  # postmodel
            app_label = eval(classname)._meta.app_label
            visualizacao_analytics = VisualizacaoDadosModel(object_id=objetoid, owner=owner,
                                                            content_type=ContentType.objects.get(
                                                                model=model, app_label=app_label)
                                                            )
            visualizacao_analytics.save()