from django.db import models

# Create your models here.

class product_PMclub(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_monarch = models.CharField(max_length=50,default="")
    product_image = models.ImageField(upload_to='images/')
    product_country = models.CharField(max_length=30)

    def __str__(self):
        return str(self.product_id)
    
