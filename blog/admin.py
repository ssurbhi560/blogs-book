from django.contrib import admin
from .models import Post #import post model to make it visible on admin page. 

# Register your models here.

admin.site.register(Post) 
