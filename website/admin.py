from django.contrib import admin
from website.models import Post, Page, UserProfile

class PostAdmin(admin.ModelAdmin):
  readonly_fields = ["slug", "date_created", "date_modified"]

admin.site.register(UserProfile)

admin.site.register(Post, PostAdmin)

admin.site.register(Page)


