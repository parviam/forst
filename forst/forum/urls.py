from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('create_poll/', views.create_poll, name='create_poll'),
    path('poll/<int:poll_id>/vote/<int:option_id>/', views.vote_poll, name='vote_poll'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('add-garden/', views.add_garden_space, name='add_garden_space'),
    path('forum/edit-garden/<int:pk>/', views.edit_garden, name='edit_garden'),
    path('forum/delete-garden/<int:pk>/', views.delete_garden, name='delete_garden'),
]
