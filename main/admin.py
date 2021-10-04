from django.contrib import admin
from .models import Users, New

admin.site.register((Users, New))
