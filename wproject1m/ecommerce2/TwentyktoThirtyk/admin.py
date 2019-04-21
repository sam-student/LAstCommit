# Register your models here.
from django.contrib import admin
from .models import TwentyktoThirtyk_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = TwentyktoThirtyk_Mobile

admin.site.register(TwentyktoThirtyk_Mobile, ProductAdmin)# Register your models here.
