from django.db import models



class Contact(models.Model):
    srl     = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=50, unique=True)
    msg     = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name