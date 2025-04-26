from django import forms
from .models import Post, Comment, Poll, PollOption

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

class PollOptionForm(forms.ModelForm):
    class Meta:
        model = PollOption
        fields = ['option_text']
