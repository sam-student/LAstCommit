# Register your models here.
from django.contrib import admin
from .models import FiveMP_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = FiveMP_Mobile

admin.site.register(FiveMP_Mobile, ProductAdmin)