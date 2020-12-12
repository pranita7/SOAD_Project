from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from blog.models import Post
from home.models import Profile
from donate.apis.serializers import PostSerializer, DonatePostSerializer, ProfileSerializer
from donate.models import Donate_Post


@api_view(http_method_names=['GET','POST',])
def post_list_view(request):
    if request.method == 'GET':
        return post_list_view_get(request)
    elif request.method == 'POST':
        return post_list_view_post(request)

@permission_classes([IsAuthenticated])
def post_list_view_get(request):
    data = Post.objects.all()
    serializer = PostSerializer(data, many=True)
    return Response(data=serializer.data)

def post_list_view_post(request):
    try:
        from django.contrib.auth import get_user_model
    except ImportError:
        from django.contrib.auth.models import User
    else:
        User = get_user_model()
    author = User.objects.get(pk=1)
    post = Post(author=author)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET',])
def post_detail_view(request,slug):
    post = Post.objects.get(title=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(http_method_names=['GET',])
def donate_post_detail_view(request,slug):
    post = Donate_Post.objects.filter(city=slug)
    serializer = DonatePostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET',])
def donate_post_all(request):
    post = Donate_Post.objects.all()
    serializer = DonatePostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['PUT',])
def donate_post_edit(request, slug):
    x = slug.split('_')
    slug = x[0]
    result = x[1]
    post = Donate_Post.objects.get(slug=slug)
    print(post.title)
    slug = post.slug
    title = post.title
    body = post.body
    city = post.city
    state = post.state
    pinCode = post.pinCode
    to_city = post.to_city
    to_state = post.to_state
    to_pinCode = post.to_pinCode
    is_requested = post.is_requested
    is_acc_for_transport = result
    serializer = DonatePostSerializer(post, data={'slug': slug, 'title': title, 'body': body, 'city':city, 'state':state, 'pinCode': pinCode, 'to_city':to_city, 'to_state': to_state, 'to_pinCode':to_pinCode,'is_requested':is_requested, 'is_acc_for_transport':is_acc_for_transport})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT'])
def profile_list_view(request):
    if request.method == 'GET':
        return profile_list_view_get(request)

def profile_list_view_get(request):
    data = Profile.objects.all()
    serializer = ProfileSerializer(data, many=True)

    return Response(data=serializer.data)

@api_view(http_method_names=['PUT', ])
def Profile_edit(request, user):
    print(user)
    x = user.split('_')
    user = int(x[0])
    coupons = int(x[1])
    print(int(x[1]))
    code1 = (x[2])
    code2 = (x[3])
    code3 = (x[4])
    print(coupons)
    print(code3)
    post = Profile.objects.get(user=user)

    city = post.city
    print(city)
    state = post.state
    clothes_donated = post.clothes_donated
    food_donated = post.food_donated
    toys_donated = post.toys_donated
    books_donated = post.books_donated
    others_donated = post.others_donated
    total_donated = post.total_donated
    pinCode = post.pinCode
    coupons_achieved = coupons
    print(coupons_achieved)
    code1 = code1
    code2 = code2
    code3 = code3
    print(coupons_achieved)
    print(type(user))
    print(type(coupons_achieved))
    serializer = ProfileSerializer(post,
                                   data={'user': user, 'city': city, 'state': state, 'clothes_donated': clothes_donated,
                                         'food_donated': food_donated, 'toys_donated': toys_donated,
                                         'books_donated': books_donated, 'others_donated': others_donated,
                                         'total_donated': total_donated, 'pinCode': pinCode,
                                         'coupons_achieved': coupons_achieved, 'code1': code1, 'code2': code2,
                                         'code3': code3})

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)



