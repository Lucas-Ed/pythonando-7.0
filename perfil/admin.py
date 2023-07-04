from django.contrib import admin

from perfil.models import Categoria, Conta


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'essencial', 'valor_planejado')
    list_filter = ('categoria', 'essencial')
    search_fields = ('categoria', 'essencial')
    list_per_page = 10


class ContaAdmin(admin.ModelAdmin):
    list_display = ('apelido', 'banco', 'tipo', 'valor')
    list_filter = ('banco', 'tipo')
    search_fields = ('apelido', 'banco', 'tipo')
    list_per_page = 10


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Conta, ContaAdmin)
