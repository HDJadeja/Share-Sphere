from django.db import models
from django.utils.text import slugify
# Create your models here.

    
class product_CCClub(models.Model):
    product_id = models.AutoField(primary_key=True)
    art_name = models.CharField(max_length=30)
    art_price = models.DecimalField(max_digits=10, decimal_places=2)
    art_description = models.CharField(max_length=30)
    art_title = models.CharField(max_length=30)
    art_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.product_id)
    