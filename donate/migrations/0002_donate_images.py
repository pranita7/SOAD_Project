# Generated by Django 3.0.3 on 2020-11-11 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='donate_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donate.Donate_Post')),
            ],
        ),
    ]
