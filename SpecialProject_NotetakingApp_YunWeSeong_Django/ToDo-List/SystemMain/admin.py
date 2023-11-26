from django.contrib import admin
from .models import SystemMainModel


# 2-line code below to show names is not working, idk why
# Register your models here.
class SystemMainAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)


admin.site.register(SystemMainModel)
