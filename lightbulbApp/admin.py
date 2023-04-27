from django.contrib import admin
from .models import Post, Comment
# Register your models here.
# Registers model with admin panel.
admin.site.register(Post)
admin.site.register(Comment)
