from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic, View

from .forms import PostForm, PostCommentForm
from .models import Post, PostComment


class PostsListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts_list'


class PostDetailView(View):
    def get(self, request, profile_id):
        post = get_object_or_404(Post, id__iexact=profile_id)
        comments = post.post_comments.all()
        form = PostCommentForm()
        if request.user.is_authenticated:
            form.fields['name'].initial = request.user
            form.fields['user'].initial = request.user
        else:
            form.fields['user'].initial = None
        return render(request, 'blog/post_detail.html', context={
            'object': post,
            'profile_id': profile_id,
            'form': form,
            'comments': comments,
        })

    def post(self, request, profile_id):
        bound_form = PostCommentForm(request.POST)
        if bound_form.is_valid():
            bound_form.save(commit=False)
            comment = PostComment()
            comment.name = bound_form.cleaned_data['name']
            comment.user = bound_form.cleaned_data['user']
            comment.comment = bound_form.cleaned_data['comment']
            comment.post = Post.objects.get(id=profile_id)
            comment.is_active = True
            if request.POST.get('parent', None):
                comment.parent_id = int(request.POST.get('parent'))
            comment.save()
            return redirect('post_detail_url', profile_id)
        return render(request, 'blog/post_detail.html', context={
            'form': bound_form,
        })


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('posts_list_url')
        return render(request, 'blog/post_create.html', context={'form': bound_form})


class PostUpdateView(View):
    def get(self, request, profile_id):
        post = Post.objects.get(id=profile_id)
        model_form = PostForm(instance=post)
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        return render(request, 'blog/post_update.html', context={
            'model_form': model_form,
            'profile_id': profile_id
        })

    def post(self, request, profile_id):
        post = Post.objects.get(id=profile_id)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            bound_form.save()
        return render(request, 'blog/post_update.html', context={
            'model_form': bound_form,
            'profile_id': profile_id
        })


class PostDeleteView(View):
    def get(self, request, profile_id):
        post = Post.objects.get(id=profile_id)
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        return render(request, 'blog/post_delete.html', context={
            'news': post,
            'profile_id': profile_id
        })

    def post(self, request, profile_id):
        post = Post.objects.get(id=profile_id)
        post.delete()
        return redirect('posts_list_url')

