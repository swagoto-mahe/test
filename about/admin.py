from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin ):
    readonly_fields = ('admin_photo',)

    def photo_tag(self, obj):
        return format_html(f'<img src="/media/(obj.image)" style="height:100px;width:100px>')

        
admin.site.register(Post,PostAdmin)

# admin.site.register(Post)