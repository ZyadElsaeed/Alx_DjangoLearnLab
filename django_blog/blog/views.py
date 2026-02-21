from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm, CustomUserCreationForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    def test_func(self): return self.request.user == self.get_object().author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    def test_func(self): return self.request.user == self.get_object().author

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)).distinct() if query else Post.objects.none()
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs.get('tag_slug')])

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save(); return redirect('login')
    else: form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
@login_required
def profile(request): return render(request, 'blog/profile.html')
