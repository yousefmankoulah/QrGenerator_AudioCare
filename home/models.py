from email.policy import default
from django.db import models

# Create your models here.

class DeviceManagment(models.Model):
    site_name= models.CharField(max_length=300)
    user_name= models.CharField(max_length=300)
    user_number= models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    qr = models.ImageField(upload_to='media', blank=True)

    class Meta:
        ordering = ('site_name',)

    def __str__(self):
        return '{}'.format(self.site_name)
