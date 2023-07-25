from django.contrib import admin
from .models import Post
# Register your models here.

# para que la spublicaciones a aparezcan en Admin
admin.site.register(Post)
