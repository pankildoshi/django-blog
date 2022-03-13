from ast import Index
from django.urls import path
from .views import AddPost, Article, Index, Profile, UpdatePost, DeletePost, LikeView, IndexLikeView
from post_module import views

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('article/<int:pk>', Article.as_view(), name="article"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('profile/', Profile.as_view(), name="profile"),
    path('article/update/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/delete/<int:pk>', DeletePost.as_view(), name="delete_post"),
    path('article/like/<int:pk>', LikeView, name='like_post'),
    path('like/<int:pk>', IndexLikeView, name='index_like_post'),
]