from django.contrib import admin
from .models import Song, UserAccount

# Register your models here.
admin.site.register(Song)
admin.site.register(UserAccount)
