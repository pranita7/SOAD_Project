from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post
from home.models import Profile
from donate.models import Donate_Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    body = serializers.CharField()
    author = serializers.RelatedField(source='User', read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'slug','body', 'author', 'author_name']

    author_name = serializers.SerializerMethodField('get_author_name')

    def get_author_name(self, obj):
        return obj.author.username

    def create(self, validated_data):
        return Post(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

class DonatePostSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    body = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    pinCode = serializers.CharField()
    to_city = serializers.CharField()
    to_state = serializers.CharField()
    to_pinCode = serializers.CharField()
    is_requested = serializers.BooleanField()
    is_acc_for_transport = serializers.BooleanField()

    def update(self, instance, validated_data):
        instance.slug = validated_data.get('slug', instance.slug)
        instance.title = validated_data.get('title',instance.title)
        instance.body = validated_data.get('body',instance.body)
        instance.city = validated_data.get('city',instance.city)
        instance.state = validated_data.get('state',instance.state)
        instance.pinCode = validated_data.get('pinCode',instance.pinCode)
        instance.to_city = validated_data.get('to_city',instance.to_city)
        instance.to_state = validated_data.get('to_state',instance.to_state)
        instance.to_pinCode = validated_data.get('to_pinCode',instance.to_pinCode)
        instance.is_requested = validated_data.get('is_requested',instance.is_requested)
        instance.is_acc_for_transport = validated_data.get('is_acc_for_transport',instance.is_acc_for_transport)
        instance.save()
        return  instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
        'user', 'city', 'state', 'clothes_donated', 'food_donated', 'toys_donated', 'books_donated', 'others_donated',
        'total_donated', 'pinCode', 'coupons_achieved', 'code1', 'code2', 'code3')