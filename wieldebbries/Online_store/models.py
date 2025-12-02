from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallInterField(null=True, Blank=True)
    phone_number = PhoneNumberField(null=True, Blank=True)
    STATUS_CHOICES = (
    ('gold', 'gold'),
    ('silver', 'silver'),
    ('bronz', 'bronz'),
    ('diamond', 'diamond')
    )
    status = models.CharField(choices=STATUS_CHOICES, default='bronz')
    date_register = models.DateTimeFiled(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_image = models.ImageField(upload_to='category_images/',)
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeingKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField('max_length=32', unique=True)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    product_name= models.CharField(max_length=64)
    price = models.PositiveInterField()
    sub_category =models.ForeingKey(SubCategory, on_delete=models.CASCADE)
    type_store = models.BooleanField()
    description = models.TextField()
    product_video = models.FileField(upload_to='product_videos/', null=True, Blank=True)
    article_number = models.PositiventerField(unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name



class ProductImage(models.Model):
    product = models.ForeingKey(Product, on_delete=models.Models.CASCADE)
    product_image - models.ImageField(upload_to='product_images/')
    def __str__(self):
        return f'{self.product}, {self.product_image}'


class Review(models.Model):
    user =models.ForeingKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeingKey(Product,  on_delete=models.CASCADE)
    rating = models.PositiventerField(choices=[(i,str(i))for i in range(1,6)])
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}, {self.product}'

class Cart(models.Model):
    user = models.OneTo0neField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeingKey(Cart, on_delete=models.CASCADE)
    product = models.ForeingKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallInterField(default=1)

    def __str__(self):
        return f'{self.product}, {self.quantity}'



