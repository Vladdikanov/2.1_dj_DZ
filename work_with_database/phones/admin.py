from django.contrib import admin

# Register your models here.
from .models import Phone
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = "name", "price", "release_date"
    list_filter = "name", "price"
    pass
