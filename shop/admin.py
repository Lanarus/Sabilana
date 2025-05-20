from django.contrib import admin
from .models import Category, Product
from .models import ProductImage, ProductVideo

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10

class ProductVideoInline(admin.StackedInline):
    model = ProductVideo
    extra = 0
    max_num = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'is_archived')
    list_filter = ('is_archived', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVideoInline]

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)