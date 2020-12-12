from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import post_list, post_create, like_post, post_edit, post_delete
from donate.apis.views import post_list_view, post_detail_view, donate_post_detail_view, donate_post_all, \
    donate_post_edit, Profile_edit, profile_list_view
from donate.views import donate_post_create, PostUpdateView, request_post, is_request_post, transport_mail
from .views import index, register, profile,rewards

urlpatterns = [
    path('', index, name='index'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile_edit/<str:user>', Profile_edit, name='profile_edit'),
    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home/logout.html'), name="logout"),
    path('posts/', post_list, name='post_list'),
    path('post_create/', post_create, name='post_create'),
    path('like/', like_post, name='like_post'),
    url(r'(?P<id>\d+)/post_edit/', post_edit, name="post_edit"),
    url(r'(?P<id>\d+)/post_delete/', post_delete, name="post_delete"),

    path('request/', request_post, name='request_post'),
    path(r'(?P<pk>\d+)/donote_post/update/', PostUpdateView.as_view(),name='donate_post_update'),
    path('donate_post_create/', donate_post_create, name='donate_post_create'),

    path('postsData/', post_list_view, name='post_list_view'),
    path('postsData/<slug:slug>', post_detail_view, name='post_detail_view'),
    path('donatePostsData/<slug:slug>', donate_post_detail_view, name='_donatepost_detail_view'),
    path('alldonatePosts/', donate_post_all, name='_donatepost_all'),
    path('donatePostEdit/<slug:slug>', donate_post_edit, name='_donatepost_edit'),
    path('rewards/', rewards,name="rewards"),
    path('apiview/',profile_list_view,name='apiview'),
    path('to_request/', is_request_post, name='is_request_post'),
    path('mail/',transport_mail,name='transport_mail'),
    # path('to/', to_receive, name='to_receive'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
