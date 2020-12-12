from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from djongo import models
from django.db.models.signals import pre_save
# Create your models here.

TYPE_CHOICES = (
        ('Clothes', 'Clothes'),
        ('Food', 'Food'),
        ('Toys', 'Toys'),
        ('Books', 'Books'),
        ('Others', 'Others')
    )

class Donate_Post(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    availableitems = models.CharField(max_length=30, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    doorNo = models.CharField(max_length=20)
    residence = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pinCode = models.IntegerField()
    to_doorNo = models.CharField(max_length=20, default=None)
    to_residence = models.CharField(max_length=40, default=None)
    to_street = models.CharField(max_length=40, default=None)
    to_city = models.CharField(max_length=30, default=None)
    to_state = models.CharField(max_length=20, default=None)
    to_country = models.CharField(max_length=20, default=None)
    to_pinCode = models.IntegerField(default=None)
    is_requested = models.BooleanField(default=False)
    to_person = models.CharField(max_length=20, default=None)
    is_acc_for_transport = models.BooleanField(default=None)
    mail_sent = models.BooleanField(default=False)
    image = models.ImageField(default="default.jpg", upload_to='donate_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

    def get_absolute_url(self):
        return reverse('profile')

@receiver(pre_save, sender= Donate_Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

