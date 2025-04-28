from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class Poll(models.Model):
    question = models.CharField(max_length=300)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.option_text

class GardenSpace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    steward = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gardens")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.strip()

class MentorshipPost(models.Model):
    ROLE_CHOICES = [
        ('steward', 'Garden Steward'),
        ('mentee', 'Mentee'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices = ROLE_CHOICES)
    content = models.TextField()
    image = models.ImageField(upload_to='mentorship_posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_role_display()} post by {self.author.username}"

class MentorshipComment(models.Model):
    ROLE_CHOICES = [
        ('steward', 'Garden Steward'),
        ('mentee', 'Mentee'),
    ]
    post = models.ForeignKey(MentorshipPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)  # Add role field
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.get_role_display()} {self.author.username}"
