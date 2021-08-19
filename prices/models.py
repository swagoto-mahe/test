from django.db import models



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title                   = models.CharField(max_length=200, unique=True)
    slug                    = models.SlugField(max_length=200, unique=True)
    updated_on              = models.DateTimeField(auto_now= True)
    header                  = models.CharField(max_length=200, blank=True)
    blank                   = models.CharField(max_length=200, blank=True)
    Monday_Friday           = models.CharField(max_length=200, blank=True)
    Saturday                = models.CharField(max_length=200, blank=True)
    sunday                = models.CharField(max_length=200, blank=True)
    Appointments            = models.CharField(max_length=200, blank=True)
    app_mon_friday_8am_6pm  = models.CharField(max_length=200, blank=True)
    app_mon_friday_6pm_10pm = models.CharField(max_length=200, blank=True)
    app_Saturday_8am_6pm    = models.CharField(max_length=200, blank=True)
    app_Sunday_8am_6pm      = models.CharField(max_length=200, blank=True)
    First_hour              = models.CharField(max_length=200, blank=True)
    First_hour_mon_friday   = models.CharField(max_length=200, blank=True)
    First_hour_moday_fri    = models.CharField(max_length=200, blank=True)
    First_hour_Saturday     = models.CharField(max_length=200, blank=True)
    First_hour_Sunday       = models.CharField(max_length=200, blank=True)
    Subsequent              = models.CharField(max_length=200, blank=True)
    Subsequent_mon_friday   = models.CharField(max_length=200, blank=True)
    Subsequent_monday_fri   = models.CharField(max_length=200, blank=True)
    Subsequent_Saturday     = models.CharField(max_length=200, blank=True)
    Subsequent_Sunday       = models.CharField(max_length=200, blank=True)
    Daily_rate	            = models.CharField(max_length=200, blank=True)
    Daily_rate_mon_frida    = models.CharField(max_length=200, blank=True)
    Daily_rate_monday_fri   = models.CharField(max_length=200, blank=True)
    Daily_rate_Saturday	    = models.CharField(max_length=200, blank=True)
    Daily_rate_sunday	    = models.CharField(max_length=200, blank=True)
    footer1                 = models.CharField(max_length=200, blank=True)
    footer2                 = models.TextField(blank=True)
    created_on              = models.DateTimeField(auto_now_add=True)
    status                  = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title