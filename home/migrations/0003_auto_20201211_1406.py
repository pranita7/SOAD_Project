# Generated by Django 3.0.3 on 2020-12-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201116_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='books_donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='clothes_donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='code1',
            field=models.CharField(default='OER', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='code2',
            field=models.CharField(default='OERIP', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='code3',
            field=models.CharField(default='OERIPLO', max_length=7),
        ),
        migrations.AddField(
            model_name='profile',
            name='coupons_achieved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='did_req',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='food_donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='others_donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='toys_donated',
            field=models.IntegerField(default=0),
        ),
    ]
