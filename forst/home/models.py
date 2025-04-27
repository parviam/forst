
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_posts', default=1)  # Default user ID
    
    def __str__(self):
        return self.text[:30]