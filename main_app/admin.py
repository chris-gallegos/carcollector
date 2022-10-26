from django.contrib import admin

# Register your models here.

from .models import Car, Show, Mod


admin.site.register(Car)
admin.site.register(Show)
admin.site.register(Mod)