from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    currency = models.CharField(max_length=10, default='F XOF')
    image = models.ImageField(upload_to='hotels/')  # sera stockée sur Cloudinary

    def __str__(self):
        return self.name
