from django.contrib import admin
from website.models import Post, Page, UserProfile

admin.site.register(UserProfile)

admin.site.register(Post)

admin.site.register(Page)
