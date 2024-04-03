from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discountPercentage = models.FloatField()
    rating = models.FloatField()
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    # customize your db products repr in admin panel
    class Meta:
        verbose_name = 'Product'
