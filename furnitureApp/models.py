from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=60, null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 209.99
    product_review = models.TextField(max_length=600, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/")
    
    def __str__(self):
        return f'{self.product_id}-{self.product_name}'
