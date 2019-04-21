# Register your models here.
from django.contrib import admin
from .models import Huawei_Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = Huawei_Product

admin.site.register(Huawei_Product, ProductAdmin)# Register your models here.
