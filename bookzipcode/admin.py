from django.contrib import admin
from .models import *



@admin.register(BookOrder)
class QuillPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)
