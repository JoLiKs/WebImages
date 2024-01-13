from django.db import models

class Image(models.Model):
    Заголовок = models.CharField(max_length=200)
    Изображение = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Заголовок