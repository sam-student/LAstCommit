# Register your models here.
from django.contrib import admin
from .models import TwelveMP_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = TwelveMP_Mobile

admin.site.register(TwelveMP_Mobile, ProductAdmin)