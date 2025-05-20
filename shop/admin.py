from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVideo
from django import forms


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
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),  # 🔥 to wymusza checkboxy
        }

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'created', 'updated', 'is_archived')
    list_filter = ('is_archived', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVideoInline]

    fields = (
        'name', 'slug', 'cart_summary', 'description',
        'categories', 'price_domestic', 'price_international',
        'available_quantity', 'is_archived'
    )



admin.site.register(Product, ProductAdmin)