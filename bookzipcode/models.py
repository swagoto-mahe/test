from django.db import models
from tinymce.models import HTMLField
from django.utils.timezone import now

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class BookOrder(models.Model):
    srl                 = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=50, blank=True)
    email               = models.EmailField(max_length=50, unique=True, blank=True)
    Ph               = models.CharField(max_length=50, blank=True)
    flat_bulding_name   = models.CharField(max_length=100, blank=True)
    street_name         = models.CharField(max_length=100, blank=True)
    postcode            = models.CharField(max_length=10, blank=True)
    service_details     = models.CharField(max_length=100, blank=True)
    infection           = models.CharField(max_length=100, blank=True)
    please_tell_us_about_your_place1     = models.CharField(max_length=100, blank=True)
    please_tell_us_about_your_place2     = models.CharField(max_length=100, blank=True)
    please_tell_us_about_your_place3     = models.CharField(max_length=100, blank=True)
    please_tell_us_about_your_place4     = models.CharField(max_length=100, blank=True)
    is_the_property_furnished_or_empty  = models.CharField(max_length=100, blank=True)
    how_would_you_like_your_carpet_to_be_cleaned  = models.CharField(max_length=100, blank=True)
    most_of_our_customers_who_book_after_builders_cleaning_also_include = models.TextField(max_length=200, blank=True)
    most_of_our_customers_who_book_after_builders_cleaning_also_include2 = models.CharField(max_length=100, blank=True)
    we_recommend_a_total_of_time_served = models.CharField(max_length=100, blank=True)
    appointment_timing_date  = models.CharField(max_length=100, blank=True)
    total_price         = models.CharField(max_length=10,blank=True)
    user_description         = HTMLField()
    note_final         = models.CharField(max_length=100,blank=True)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    # title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    
    Commercial_Cleaning_price = models.IntegerField(blank=True,null=True)
    Domestic_Cleaning_price = models.IntegerField(blank=True,null=True)
    Residential_Cleaning_price    = models.IntegerField(blank=True,null=True)
    infection_control_cleaning_services_yes = models.IntegerField(blank=True, null=True)
    infection_control_cleaning_services_No = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']



    

    

        