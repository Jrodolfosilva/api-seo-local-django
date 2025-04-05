from django.contrib import admin
from br.models import Cidade
from br.models import Estado
from br.models import Bairro
# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)