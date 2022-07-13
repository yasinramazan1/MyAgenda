from django.db import models
from datetime import datetime
# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank = True) 
    # blank özelliği ile boş geçilip geçilmeme durumunu kontrol ediyoruz.
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)
    # Burada bir model oluşturduk, ancak kaydettiğimizde bunun kaydolmadığını görürüz.
    # O yüzden bunları veritabanına göndermeliyiz. Yani migrate komutu ile migration yapılmalıdır.
    # Proje dosyasının içinde python manage.py makemigrations komutu ile 
    # bunları veritabanınına kaydetmemiz gerekir.
    # Ardından yine proje dosyası dizininde iken python manage.py migrate komutu ile
    #  bu kayıtları da veritabanına göndermemiz gerekir.
    def __str__(self):
        return self.title
        # __str__() metodu, ilk başta admin paneline gelen kayıtların isimlerinin standart 
        # görünmesini değiştirmek ve yuakrıdaki belirttiğimiz bir özelliğin admin panelindes
        # başlık olarak görünmesini sağlamaktadır.
    
