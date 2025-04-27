from django.db import models
from django.utils import timezone

class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]
# Create your models here.
