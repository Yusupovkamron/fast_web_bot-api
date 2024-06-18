from django.db import models
from django.contrib.auth.models import User
from .help import SaveMediaFile



class Product(models.Model):
    class PriceType(models.TextChoices):
        sum = "som"
        s = "$"


    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField
    price = models.FloatField()
    image = models.ImageField(upload_to=SaveMediaFile.customer_image_path)
    price_type = models.CharField(max_length=20, choices=PriceType.choices, default=PriceType.sum)
    count = models.PositiveBigIntegerField()
    category_data = models.DateTimeField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'product'


    def __str__(self):
        return self.name



class Orders(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=1)
    last_update = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=SaveMediaFile.customer_image_path)
    locatsiya = models.CharField(max_length=50)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.locatsiya



class Discount(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    new_price = models.FloatField()
    image = models.ImageField(upload_to="webapp/discount/")
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to=SaveMediaFile.customer_image_path)
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    Comment = models.CharField(max_length=300)
    image = models.ImageField(upload_to=SaveMediaFile.customer_image_path)
    product = models.ManyToManyField(Product)
    last_update = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


