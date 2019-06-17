from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length = 255)
    konten = models.TextField()
    terbit = models.DateTimeField(default = timezone.now)
    nama = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})