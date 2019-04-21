# Register your models here.
from django.contrib import admin
from .models import TenktoTwentyk_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = TenktoTwentyk_Mobile

admin.site.register(TenktoTwentyk_Mobile, ProductAdmin)# Register your models here.
