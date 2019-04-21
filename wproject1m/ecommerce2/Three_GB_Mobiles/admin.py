# Register your models here.
from django.contrib import admin
from .models import Three_GB_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = Three_GB_Mobile

admin.site.register(Three_GB_Mobile, ProductAdmin)# Register your models here.
