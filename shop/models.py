from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Category Name"))
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name=_("Product Name"))
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True, verbose_name=_("Description"))
    cart_summary = models.CharField(
        max_length=255,
        default="Default cart summary",
        verbose_name=_("Cart Summary"),
        help_text=_("Short description that will appear in the cart")
    )

    categories = models.ManyToManyField(Category, related_name="products", verbose_name=_("Categories"))
    price_domestic = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name=_("Domestic Price"))
    price_international = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("International Price"))

    available_quantity = models.PositiveIntegerField(default=1, verbose_name=_("Available Quantity"))
    is_archived = models.BooleanField(default=False, verbose_name=_("Archived"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=100, verbose_name=_("Variant Name"))
    color = models.CharField(max_length=50, blank=True, verbose_name=_("Color"))
    material = models.CharField(max_length=100, blank=True, verbose_name=_("Material"))

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")

    def __str__(self):
        return f"{self.product.name} – {self.name}"

