from django.contrib import admin
from posts.models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","title", "updated", "timestamp"]
    list_display_links = ["id"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)
