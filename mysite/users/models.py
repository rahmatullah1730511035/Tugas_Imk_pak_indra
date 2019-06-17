from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        gambar = Image.open(self.image.path)

        if gambar.height > 300 or gambar.width > 300:
            output_size = (300,300)
            gambar.thumbnail(output_size)
            gambar.save(self.image.path)