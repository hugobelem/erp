from django.contrib import admin

from .models import Empresa, Cliente, Produto, Pedido, PedidoItem


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoItemInline]

admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)