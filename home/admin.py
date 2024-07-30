from django.contrib import admin
from home.models import Contact, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price')

admin.site.register(Contact)
admin.site.register(Product, ProductAdmin)