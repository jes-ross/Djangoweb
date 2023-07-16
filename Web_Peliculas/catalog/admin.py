from django.contrib import admin

# Register your models here.
from .models import Genre, Film, Director

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Director)
