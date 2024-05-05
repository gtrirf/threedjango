from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    nameproduct = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    body = models.TextField()
    price = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.nameproduct