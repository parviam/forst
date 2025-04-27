from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PostForm
from .models import Post
def index(request):
    template_data = {}
    template_data['title'] = 'Forst'
    return render(request, 'home/index.html', {
        'template_data': template_data
    })
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {
        'template_data': template_data
    })
def maps(request):
    template_data = {}
    template_data['title'] = 'Maps'
    return render(request, 'home/maps.html', {
        'template_data': template_data,
        'maps_api_key': settings.MAPS_API_KEY
    })
def notebook(request):
    # Get all posts from the database, ordered by creation date (newest first)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home/notebook.html', {'posts': posts})
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home.notebook')  # or wherever you want to go after submitting
    else:
        form = PostForm()
    return render(request, 'home/new_post.html', {'form': form})
# Create your views here.
