from django.contrib import admin
from .models import Post, User, Comment, Like, PostView
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'content', 'publish_date', ]


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
