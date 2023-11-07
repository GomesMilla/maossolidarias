from django.contrib import admin
from .models import User, Estado, Cidade, DenunciarEmpresa

admin.site.register(User)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(DenunciarEmpresa)

