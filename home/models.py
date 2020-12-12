from django.contrib.auth.models import User
from django.db import models
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    city = models.CharField(max_length=30,default=None)
    state = models.CharField(max_length=20,default=None)
    pinCode = models.IntegerField(default=None)
    did_req = models.BooleanField(default=False)
    clothes_donated = models.IntegerField(default=0)
    food_donated = models.IntegerField(default=0)
    toys_donated = models.IntegerField(default=0)
    books_donated = models.IntegerField(default=0)
    others_donated = models.IntegerField(default=0)
    total_donated = models.IntegerField(default=0)
    coupons_achieved = models.IntegerField(default=0)
    code1 = models.CharField(max_length=3, default="OER")
    code2 = models.CharField(max_length=5, default="OERIP")
    code3 = models.CharField(max_length=7, default="OERIPLO")
    phoneno = models.CharField(max_length=13,default='+916303844857')
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width>300:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)