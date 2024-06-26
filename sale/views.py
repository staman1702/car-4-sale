from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm, CommentAdminForm, PostForm, PostAdminForm


class PostList(generic.ListView):
    model = Post
    template_name = "sale/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Post.objects.all()
            else:
                return Post.objects.filter(
                    Q(author=user) | Q(status=1)
                )
        else:
            return Post.objects.filter(status=1)


def post_detail(request, slug):

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                comment_form = CommentAdminForm(data=request.POST)
            else:
                comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()

                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )
        else:
            messages.error(request, 'You need to be logged in to post comments.')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if request.user.is_superuser:
        comment_form = CommentAdminForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "sale/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def comment_edit(request, slug, comment_id):

    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user.is_superuser:
            comment_form = CommentAdminForm(data=request.POST, instance=comment)
        else:
            comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and (comment.author == request.user or request.user.is_superuser):
            comment = comment_form.save(commit=False)
            comment.post = post
            if not request.user.is_superuser:
                comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')

        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_post(request):
    """
    View to add a new post.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Error creating post!')
    else:
        form = PostForm(user=request.user)

    return render(request, 'sale/add_post.html', {'form': form})


@login_required
def edit_post(request, slug):
    """
    View to edit an existing post.
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        if request.user.is_superuser:
            form = PostAdminForm(request.POST, request.FILES, instance=post, user=request.user)
        else:
            form = PostForm(request.POST, request.FILES, instance=post, user=request.user)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.save()
            messages.success(request, 'Post updated successfully!')
            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Error updating post!')
    else:
        if request.user.is_superuser:
            form = PostAdminForm(instance=post, user=request.user)
        else:
            form = PostForm(instance=post, user=request.user)

    return render(request, 'sale/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    """
    View to delete a post.
    """
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_superuser and request.user != post.author:
        messages.error(request, 'Sorry, only sales post creator/site admin can do that.')
        return redirect('post_detail', slug=slug)

    post.delete()
    messages.success(request, 'Sales post deleted!')

    return redirect('home')
