from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
import requests
# Create your views here.
from donate.models import Donate_Post
from home.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from home.models import Profile


def index(request):
    if request.user.is_authenticated:
        prof = Profile.objects.get(user=request.user)
        print(prof.user)
        if (prof.city==None or prof.state==None or prof.pinCode==None):
            print("complete profile plis")
            messages.success(request, f'Please complete your Profile {prof.user} .... by going to profile and filling your address details!')
    return render(request, 'home/homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})


@login_required
def profile(request):
    posts = Donate_Post.objects.filter(author=request.user).order_by('-created')
    Cposts = Donate_Post.objects.filter(author=request.user).filter(availableitems="Clothes")
    Fposts = Donate_Post.objects.filter(author=request.user).filter(availableitems="Food")
    Tposts = Donate_Post.objects.filter(author=request.user).filter(availableitems="Toys")
    Bposts = Donate_Post.objects.filter(author=request.user).filter(availableitems="Books")
    Oposts = Donate_Post.objects.filter(author=request.user).filter(availableitems="Others")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'Cposts': Cposts,
        'u_form': u_form,
        'p_form': p_form,
        'posts': posts,
        'Fposts': Fposts,
        'Tposts': Tposts,
        'Bposts': Bposts,
        'Oposts': Oposts
    }
    return render(request, 'home/profile.html', context)


def rewards(request):
    post = get_object_or_404(Profile, user=request.user)
    if post.coupons_achieved == 0:
        messages.info(request, f'No coupouns recieved till now.')

    context = {
        'post': post,

    }
    return render(request, 'home/rewards.html', context)