from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import tweepy
# Create your views here.
from blog.forms import PostCreateForm, PostEditForm
from blog.models import Post, Images
from django.forms import modelformset_factory
consumer_key="unWC0suaCTgUnlNOBNTcnVOl5"
consumer_secret="SgnnmXjBVK752lM0yjas40r3n1u6ljXVNO4mJmenX9gMg90YcL"
access_token = "1335676715801092101-ZsKtRF8jU9MgHvxORky5Dii4oy4U3m"
access_token_secret="nRFVy3Ew3vkqDSANTJW3WMyn1tgq5BThlCnEaW5tVo9HT"

@login_required
def post_list(request):
    post_list = Post.objects.all().order_by('-id')
    for post in post_list:
        post.total = post.total_likes()
        post.is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.is_liked = True
            post.save()
    query = request.GET.get('q')
    if query:
        post_list = Post.objects.filter(
            Q(author__username=query)
        )
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagenation(posts, index=2)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'posts': posts,
        'page_range': page_range,
    }
    return render(request, 'blog/post_list.html', context)

def proper_pagenation(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return  (start_index, end_index)

@login_required
def post_create(request):
    ImageFormset = modelformset_factory(Images, fields=('image',))
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for f in formset:
                try:
                    photo = Images(post=post, image=f.cleaned_data['image'])
                    photo.save()
                    return redirect('post_list')
                except Exception as e:
                    break
            messages.success(request, f'Post created successfully!')

        def OAuth():
            try:
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                return auth
            except Exception as e:
                return None

        def tweet():
            oauth = OAuth()
            api = tweepy.API(oauth)
            posts = Post.objects.filter(posted=False)
            for post in posts:
                post.posted = True
                post.save()
                string1 = post.author
                string2 = "expressing his gratitude for help recieved through our Helpers.org."
                stri = post.author
                strii = ":"
                strin = post.body
                string3 = f"{string1} {string2} {stri} {strii} {strin}"
                api.update_status(string3)

                print('a tweet is posted')

        tweet = tweet()
        return redirect('post_list')
    else:
        form = PostCreateForm()
        formset = ImageFormset(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'blog/post_create.html',context)


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        raise Http404()
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)

        if form.is_valid():
            print("hi")
            form.save()
            #print(formset.cleaned_data)

            return redirect('post_list')
    else:
        form = PostEditForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/post_edit.html', context)


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.is_liked = False
        post.save()
    else:
        post.likes.add(request.user)
        post.is_liked = True
        post.save()
    return redirect('post_list')

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        raise Http404()
    post.delete()
    return redirect('post_list')