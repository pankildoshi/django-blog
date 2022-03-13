from dataclasses import fields
from re import template
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def index(request):
#     return render(request, 'index.html', {})

class Index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']
    # ordering = ['-id']

class Article(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = data.total_likes()
        context['total_likes'] = total_likes
        return context

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
    # form_class = PostForm

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = [
        'title', 'headline', 'content'
    ]

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class Profile(ListView):
    model = Post
    template_name = 'profile.html'
    ordering = ['-post_date']

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))

def login(request):
    return render(request, 'login.html', {})

# # Create your views here.
# class PostView(ListView):
#     model = Post
#     template_html = 'index.html'