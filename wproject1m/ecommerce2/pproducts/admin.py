# Register your models here.
from django.contrib import admin
from .models import P_Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = P_Product

admin.site.register(P_Product, ProductAdmin)