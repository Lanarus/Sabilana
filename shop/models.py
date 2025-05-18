from django.db import models
from django.utils.translation import gettext_lazy as _

# gettext_lazy pozwala tłumaczyć nazwy pól w panelu admina — potrzebne do wielojęzyczności.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name"))
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

# Category: nazwa i slug (czyli przyjazna URL-owa wersja nazwy)
#Product: odnosi się do kategorii, ma cenę, dostępność i daty.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Product Name"))
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, verbose_name=_("Description"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name=_("Category"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    is_available = models.BooleanField(default=True, verbose_name=_("Available"))
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
