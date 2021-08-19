from django.db import models
from django.utils.safestring import  mark_safe

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    middel = models.CharField(max_length=200)
    content = models.TextField()
    image   =   models.ImageField()
    header  =   models.CharField(max_length=200, blank=True)
    heade2  =   models.TextField(max_length=200, blank=True)
    footer_header   =   models.CharField(max_length=200, blank=True)
    foter_description = models.TextField(blank=True)
    footer_image_1  =   models.ImageField(blank=True)
    footer_image_1_header  =   models.CharField(max_length=200,blank=True)
    footer_image_1_description  =   models.TextField(blank=True)
    footer_image_2  =   models.ImageField(blank=True)
    footer_image_2_header  =   models.CharField(max_length=200,blank=True)
    footer_image_2_description  =   models.TextField(blank=True)
    side_image  =   models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.footer_image_1.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    

