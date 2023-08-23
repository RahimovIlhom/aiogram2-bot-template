from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    mention = models.CharField(max_length=120)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='data/images/', null=True, blank=True)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return f"{self.brand}"

