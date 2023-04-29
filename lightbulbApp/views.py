from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


# fields are already created in loginview template
class myLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("PostList")


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('created')
    template_name = 'index.html'
    paginate_by = 6


class Comments(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.order_by('created')
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created")
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
