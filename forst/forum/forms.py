from django import forms
from .models import Post, Comment, Poll, PollOption, MentorshipPost, MentorshipComment

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
# forms.py
from django import forms
from .models import GardenSpace

class GardenSpaceForm(forms.ModelForm):
    class Meta:
        model = GardenSpace
        fields = ['name', 'description']

class MentorshipPostForm(forms.ModelForm):
    class Meta:
        model = MentorshipPost
        fields = ['role', 'content', 'image']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

class MentorshipCommentForm(forms.ModelForm):
    class Meta:
        model = MentorshipComment
        fields = ['role', 'content']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }