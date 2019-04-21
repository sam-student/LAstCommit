# Register your models here.
from django.contrib import admin
from .models import A_Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = A_Product

admin.site.register(A_Product, ProductAdmin)