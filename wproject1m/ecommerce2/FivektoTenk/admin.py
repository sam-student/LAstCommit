# Register your models here.
from django.contrib import admin
from .models import FivektoTenk_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = FivektoTenk_Mobile

admin.site.register(FivektoTenk_Mobile, ProductAdmin)# Register your models here.
