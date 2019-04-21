# Register your models here.
from django.contrib import admin
from .models import One_GB_Mobile

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = One_GB_Mobile

admin.site.register(One_GB_Mobile, ProductAdmin)# Register your models here.
