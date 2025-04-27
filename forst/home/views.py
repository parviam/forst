from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = []
        message = "You need to log in to view your posts."
    
    return render(request, 'home/notebook.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the logged-in user as the author
            post.save()  # Save the post
            return redirect('home.notebook')  # Redirect to the notebook page
    else:
        form = PostForm()

    return render(request, 'home/new_post.html', {'form': form})

# Create your views here.
