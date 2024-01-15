from django.db import models
from django.contrib.auth.models import User
class Image(models.Model):
    Заголовок = models.CharField(max_length=200)
    Изображение = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Заголовок


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'