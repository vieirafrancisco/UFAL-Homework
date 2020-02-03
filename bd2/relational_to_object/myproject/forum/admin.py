from django.contrib import admin

from .models import Post, Admin, CommonUser, Topic, Comment, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Admin)
admin.site.register(CommonUser)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Tag)
