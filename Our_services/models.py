from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    header = models.CharField(max_length=200)
    content = models.TextField()
    contaners = models.TextField()
    title_prices = models.IntegerField()
    ul_1 = models.CharField(max_length=200, blank=True)
    ul_2 = models.CharField(max_length=200, blank=True)
    ul_3 = models.CharField(max_length=200, blank=True)
    ul_4 = models.CharField(max_length=200, blank=True)
    ul_5 = models.CharField(max_length=200, blank=True)
    ul_6 = models.CharField(max_length=200, blank=True)
    ul_7 = models.CharField(max_length=200, blank=True)
    ul_8 = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)
    experienced_staff_1                 =   models.CharField(max_length=200, blank=True)
    experienced_staff_description_1     =   models.TextField (blank=True)
    experienced_s_images                =   models.ImageField(blank=True)
    experienced_staff_2                 =   models.CharField(max_length=200, blank=True)
    experienced_staff_description_2     =   models.TextField(blank=True)
    experiencedimg                 =   models.ImageField(blank=True, null=True)
    experienced_staff_3                 =   models.CharField(max_length=200,blank=True)
    experienced_staff_description_3     =   models.TextField(blank=True)
    experiencedsta_imagessss                =   models.ImageField(blank=True)
    experienced_staff_4                 =   models.CharField(max_length=200,blank=True)
    experienced_staff_description_4     =   models.TextField(max_length=200,blank=True)
    experienced_stafimagess               =   models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        