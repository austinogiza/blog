from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Like, PostView, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm
# Create your views here.


class HomeView(ListView):

    model = Post
    paginate_by = 10
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            form.user = self.request.user
            form.comment = form.cleaned_data.get('comment')
            form.post = post

            comment = Comment(
                user=form.user,
                content=form.comment,
                post=form.post
            )
            comment.save()
            return redirect('blog:detail', slug=post.slug)
        return redirect('blog:detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object


@login_required
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        messages.error(request, "Oh no!! You just unliked the post")
        return redirect('blog:detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    messages.success(request, "Yay!! You just liked the post")
    return redirect('blog:detail', slug=slug)
