from django.contrib import admin
from website.models import Post, Page, UserProfile

class PostAdmin(admin.ModelAdmin):
  readonly_fields = ["slug",]

admin.site.register(UserProfile)

admin.site.register(Post, PostAdmin)

admin.site.register(Page)


