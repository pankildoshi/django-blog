from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class Index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

class Article(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

class AddComment(CreateView):
    model = Comment
    template_name = 'article.html'
    fields = [
        'post', 'name', 'body'
    ]

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = [
        'title', 'headline', 'content', 'featured_image'
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
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))

def IndexLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('index'))

def login(request):
    return render(request, 'login.html', {})

# # Create your views here.
# class PostView(ListView):
#     model = Post
#     template_html = 'index.html'