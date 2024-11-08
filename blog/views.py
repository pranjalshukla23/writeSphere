from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# home view function
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # passing posts as context to home template
    return render(request, 'blog/home.html', context)

# class based model
# ListView is used to fetch and display records
class PostListView(ListView):
    # which model to query
    model = Post
    
    # which template to render
    template_name = "blog/home.html"
    
    # set the name of the context object
    context_object_name = "posts"
    
    # sort records by date_posted
    ordering = ["-date_posted"]
    
    # have 2 posts per page and use pagination functionality
    paginate_by = 2
    
# class based model
# ListView is used to fetch and display records
class UserPostListView(ListView):
    # which model to query
    model = Post
    
    # which template to render
    template_name = "blog/user_posts.html"
    
    # set the name of the context object
    context_object_name = "posts"
    
    # sort records by date_posted
    ordering = ["-date_posted"]
    
    # have 2 posts per page and use pagination functionality
    paginate_by = 2
    
    def get_queryset(self):
        # get the user object passed in the parameter
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        # get posts related to the user
        return Post.objects.filter(author=user).order_by("-date_posted")
        
    
    
# class based model
# DetailView is used to read information of a specific object
class PostDetailView(DetailView):
    # which model to query
    model = Post
    
    # By default, DetailView uses the context object name "object"
    
    # By default, DetailView uses the template name "app/modelName_viewName.html"
    
# class based model
# DetailView is used to create new records
class PostCreateView(LoginRequiredMixin, CreateView):
    # which model to query
    model = Post
    
    # which fields to have in form
    fields = ["title", "content"]
    
    
    # overriding the form save method
    def form_valid(self, form):
        # add an author field to the instance
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# class based model
# UpdateView is used to update existing records
# adding conditions using mixin (eg LoginRequiredMixin) to ensure only logged in user access this route
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # which model to query
    model = Post
    
    # which fields to have in form
    fields = ["title", "content"]
    
    # overriding the form save method
    def form_valid(self, form):
        # add an author field to the instance
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # test that needs to be passed before updating the post
    def test_func(self):
        post = self.get_object()
        # check if the logged in user is the author of the post
        if self.request.user == post.author:
            return True
        return False

# class based model
# DeleteView is used to delete a specific object
# adding conditions using mixin (eg LoginRequiredMixin) to ensure only logged in user access this route
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # which model to query
    model = Post
    
    # redirect to home page when the post is deleted
    success_url = "/"
    
    # By default, DeleteView uses the context object name "object"
    
    # By default, DetailView uses the template name "app/modelName_confirm_viewName.html"
    
    # test that needs to be passed before deleting the post
    def test_func(self):
        post = self.get_object()
        # check if the logged in user is the author of the post
        if self.request.user == post.author:
            return True
        return False            
    

# about view function
def about(request):
    # passing title as context to about template
    return render(request, 'blog/about.html', {'title': 'About'})
