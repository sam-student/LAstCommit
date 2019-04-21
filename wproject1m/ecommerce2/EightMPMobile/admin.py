# Register your models here.
from django.contrib import admin
from .models import EightMP_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = EightMP_Mobile

admin.site.register(EightMP_Mobile, ProductAdmin)