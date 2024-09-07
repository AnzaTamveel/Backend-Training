from django.shortcuts import render
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


def base_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "base.html", context)

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)

    similar_category_posts = Post.objects.filter(categories__in=post.categories.all()).exclude(pk=post.pk).distinct()

    categories = Category.objects.all()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "categories": categories,
        "similar_category_posts": similar_category_posts,
    }
    return render(request, "blog/detail.html", context)