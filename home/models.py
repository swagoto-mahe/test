from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    wellcome_msg            =   models.CharField(max_length=200, blank=True)
    wellcome_msg3           =   models.TextField(blank=True)
    best_team               =   models.CharField(max_length=200,blank=True)
    commercial_cleaning     =   models.TextField(blank=True)
    commercial_description  =   models.TextField(blank=True)
    commercial_image        =   models.ImageField(blank=True)
    dom_residentiam_clean   =   models.TextField(blank=True)
    dom_residentiam_description   =   models.TextField(blank=True)
    dom_residentiam_image   =   models.ImageField(blank=True)
    cleaning_services       = models.CharField(max_length=200, blank=True)
    maintenance_services    =   models.TextField(blank=True)
    maintenance_image       =   models.ImageField(blank=True)
    maintenance_description =   models.TextField(blank=True)
    covid_disinfection      =   models.TextField(blank=True)
    covid_image             =   models.ImageField(blank=True)
    covid_description       =   models.TextField(blank=True)
    content                 = models.TextField(blank=True)
    what_makes_your_service = models.CharField(max_length=200, blank=True)
    services_1 = models.CharField(max_length=200, blank=True)
    services_2 = models.CharField(max_length=200, blank=True)
    services_3 = models.CharField(max_length=200, blank=True)
    services_4 = models.CharField(max_length=200, blank=True)
    services_5 = models.CharField(max_length=200, blank=True)
    services_6 = models.CharField(max_length=200, blank=True)
    services_7 = models.CharField(max_length=200, blank=True)
    services_8 = models.CharField(max_length=200, blank=True)
    services_9 = models.CharField(max_length=200, blank=True)
    services_10 = models.CharField(max_length=200, blank=True)
    services_11 = models.CharField(max_length=200, blank=True)
    services_12 = models.CharField(max_length=200, blank=True)
    services_13 = models.CharField(max_length=200, blank=True)
    services_14 = models.CharField(max_length=200, blank=True)
    services_15 = models.CharField(max_length=200, blank=True)
    services_16 = models.CharField(max_length=200, blank=True)
    services_17 = models.CharField(max_length=200, blank=True)
    services_18 = models.CharField(max_length=200, blank=True)
    services_19 = models.CharField(max_length=200, blank=True)
    services_20 = models.CharField(max_length=200, blank=True)
    what_make_image = models.ImageField(blank =True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
