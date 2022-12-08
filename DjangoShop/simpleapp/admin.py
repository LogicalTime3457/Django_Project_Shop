from django.contrib import admin
from .models import Category, Product, Material, ProductMaterial


#Добавляем в админ панель строку, где можно будет выбрать материал продукта
class ProductMaterialInLine(admin.TabularInline):
    model = ProductMaterial
    fk_name = 'product'
    extra = 1


#Продолжаем добавлять настройки для выбора материала
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMaterialInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)#ProductAdmin добавили, чтобы изменить админ-панель
admin.site.register(Material)

