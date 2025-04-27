from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Poll, PollOption, GardenSpace
from .forms import PostForm, CommentForm, PollForm, PollOptionForm
from django.contrib.auth.decorators import login_required
from .forms import GardenSpaceForm

def forum_home(request):

    posts = Post.objects.all().order_by('-created_at')
    polls = Poll.objects.all().order_by('-created_at')

    if request.user.is_authenticated:
        user_gardens = GardenSpace.objects.filter(steward=request.user)
    else:
        user_gardens = []

    return render(request, 'forum/forum_home.html', {
        'posts': posts,
        'polls': polls,
        'user_gardens': user_gardens,
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Attach the currently logged-in user
            post.save()
            return redirect('forum_home')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})


@login_required
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('view_post', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'forum/view_post.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        option_forms = [PollOptionForm(request.POST, prefix=str(x)) for x in range(0, 3)]  # 3 options

        if poll_form.is_valid() and all([of.is_valid() for of in option_forms]):
            poll = poll_form.save(commit=False)
            poll.created_by = request.user
            poll.save()

            for option_form in option_forms:
                option = option_form.save(commit=False)
                option.poll = poll
                option.save()

            return redirect('forum_home')
    else:
        poll_form = PollForm()
        option_forms = [PollOptionForm(prefix=str(x)) for x in range(0, 3)]

    return render(request, 'forum/create_poll.html', {
        'poll_form': poll_form,
        'option_forms': option_forms
    })

@login_required
def vote_poll(request, poll_id, option_id):
    option = get_object_or_404(PollOption, id=option_id, poll_id=poll_id)
    option.votes += 1
    option.save()
    return redirect('forum_home')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('forum_home')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  # Save post ID before deleting
    if request.user == comment.author:
        comment.delete()
    return redirect('view_post', post_id=post_id)

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user == poll.created_by:
        poll.delete()
    return redirect('forum_home')
@login_required
def add_garden_space(request):
    if request.method == 'POST':
        form = GardenSpaceForm(request.POST)
        if form.is_valid():
            garden = form.save(commit=False)
            garden.steward = request.user
            garden.save()
            return redirect('forum_home')
    else:
        form = GardenSpaceForm()
    
    return render(request, 'forum/add_garden_space.html', {'form': form})
@login_required
def edit_garden(request, pk):
    # Get the garden object
    garden = get_object_or_404(GardenSpace, pk=pk)

    # If the request is a POST (form submission), process the form
    if request.method == 'POST':
        form = GardenSpaceForm(request.POST, instance=garden)
        if form.is_valid():
            form.save()
            return redirect('forum_home')  # Redirect to the forum home page after saving
    else:
        form = GardenSpaceForm(instance=garden)

    return render(request, 'forum/edit_garden.html', {'form': form, 'garden': garden})
@login_required
def delete_garden(request, pk):
    # Get the garden object by primary key (pk)
    garden = get_object_or_404(GardenSpace, pk=pk)

    # Delete the garden object
    garden.delete()

    # Redirect the user to the forum home page after deletion
    return redirect('forum_home')
