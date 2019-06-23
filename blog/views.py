from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, PostComment
from .forms import PostCommentForm
from django.contrib import messages


def archive(request):
    posts = Post.objects.all().order_by('-published')
    return render(request, 'archive-blog.html', {'items': posts})


def single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment has been added")
            return redirect(reverse('blog_single', kwargs={'pk': pk}))
        else:
            messages.error(request, "To add the comment you need to login")
            return redirect('login')
    comment_form = PostCommentForm()
    comments = PostComment.objects.filter(post__pk=post.pk)

    return render(request, 'single-post.html', {'item': post,
                                                'comments': comments,
                                                'body_class': 'single_post_blog',
                                                'comments_form': comment_form})
