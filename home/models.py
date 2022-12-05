from email.policy import default
from django.db import models

# Create your models here.

class DeviceManagmentService(models.Model):
    site_name= models.CharField(max_length=300)
    site_type= models.CharField(max_length=300)
    serial_number= models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    qr = models.ImageField(upload_to='media', blank=True)

    class Meta:
        ordering = ('site_name',)

    def __str__(self):
        return '{}'.format(self.site_name)
