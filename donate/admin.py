from django.contrib import admin

# Register your models here.
from donate.models import Donate_Post

class DonatePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'city', 'state', 'country')
    list_filter = ['created', 'updated']
    search_fields = ['author__username', 'city', 'state']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Donate_Post, DonatePostAdmin)