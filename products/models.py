from operator import mod
from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return f'{float(self.price) * 1.3}'

    def get_discount(self):
        return '123'

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
