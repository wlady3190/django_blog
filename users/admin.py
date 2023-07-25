from django.contrib import admin
# luego de crear el modelo para la craga de imagenes, se importa aqui
from .models import Profile
# Register your models here.

admin.site.register(Profile)

# con esto se crearn la imagenes dentro del propio documento, lo cual no es bueno. Se debe cambiar la localizacion donde se guardan las imagenes en Settings.py


