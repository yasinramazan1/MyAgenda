from django.contrib import admin
from .models import Todos 
# Burada models dosyasında oluşturulan Todos sınıfını import ederek 
# eklediğimiz yeni işlerin de admin sayfasında görünmesini sağladık.
# Register your models here.
admin.site.register(Todos) 
# register() metodu, yaptığımız işlerin kaydını admin paneline de kaydetmeye yarar. 