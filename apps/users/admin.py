from django.contrib import admin
from .models import User, Estado, Cidade

admin.site.register(User)
admin.site.register(Estado)
admin.site.register(Cidade)

