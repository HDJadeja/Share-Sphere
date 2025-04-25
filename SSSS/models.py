from django.db import models

# Create your models here.\

class SSSS_products(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=100,decimal_places=2)
    product_artist = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product_name
    
class SSSS_artist(models.Model):
    artist_id = models.IntegerField()
    artist_name = models.CharField(max_length=100)
    artist_image = models.ImageField(upload_to='images')
    artist_description = models.CharField(max_length=500)

    def __str__(self):
        return self.artist_name

