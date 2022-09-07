from django.contrib import admin
from .models import Produto, Categoria


class Products(admin.ModelAdmin):
    list_display = ('id','name','category','price','description')


class Category(admin.ModelAdmin):
    list_display = ('id','category_name')


admin.site.register(Produto, Products)
admin.site.register(Categoria, Category)