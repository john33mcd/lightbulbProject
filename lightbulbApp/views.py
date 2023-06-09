from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic.edit import CreateView, FormView, UpdateView


# fields are already created in loginview template

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('created')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.order_by('created')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )

# views and functionality codeblocks for login and registration
# taken from youtube tutorial, more in readMe


class MyLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post_form.html'
    success_url = reverse_lazy('index')


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('index')