from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.contrib import messages
from .models import Post
# from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "sale/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`sale.Post`.

    **Context**

    ``post``
        An instance of :model:`sale.Post`.

    **Template:**

    :template:`sale/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "sale/post_detail.html", {"post": post},)
