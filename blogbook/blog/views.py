from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


#ListView
class PostListView(ListView):
    model = Post # to specify the model to query a model to create a post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post # to specify the model to query a model to create a post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

#filtering by user. get it from the url. SO getting the user. if user exits fine else 404
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
        model = Post  # to specify the model to query a model to create a post

#View to create posts[title,content for new post,date_posted will be created automatically]
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # to specify the model to query a model to create a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #befor submitting,set the current user as author
        return super().form_valid(form) #we run the parent form and we pass the overridden form also


#Update Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # to specify the model to query a model to create a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #befor submitting,set the current user as author
        return super().form_valid(form) #we run the parent form and we pass the overridden form also

    # To make sure that only u update your post and not allow others to update it , UserPassesTextMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return  False

#User should be logged in and the author can only delete the view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #redirects to homepage after deletion
# To make sure that only u update your post and not allow others to update it , UserPassesTextMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')

