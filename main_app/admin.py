from django.contrib import admin

# Register your models here.

from .models import Car, Show


admin.site.register(Car)

admin.site.register(Show)