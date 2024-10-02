from django.contrib import admin

from .models import Business, Product, Order, OrderItem

admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)