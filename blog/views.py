from django.views import generic
from .import models
from .form import CommentForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


class BlogIndex(generic.ListView):
    queryset = models.Entry.object.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"


def add_comment_to_post(request, slug):
    entry = get_object_or_404(models.Entry, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entry = entry
            comment.save()
            return redirect('entry_detail', slug=entry.slug)
    else:
            form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, slug):
    comment = get_object_or_404(request, slug=slug)
    comment.approve()
    return redirect('entry_detail', slug=comment.slug)

@login_required
def comment_remove(request, slug):
    comment = get_object_or_404(request, slug=slug)
    comment.delete()
    return redirect('entry_detail', slug=comment.slug)

