from django.db import models
from django.utils.text import slugify

# Create your models here.
class Pro_Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Flavor(models.Model):
    name = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.product_type})"
    
class StatusType(models.IntegerChoices):
    publish = 0, 'able to show'
    draft = 1, 'unable to show'

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    flavor = models.ForeignKey(Flavor, on_delete=models.SET_NULL, null=True, blank=True)
    pro_category = models.ForeignKey(Pro_Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True, default='product/question_mark.jpg')
    available = models.BooleanField(default=True)
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.draft.value)
    created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_final_price(self):
        if self.discount_percent:
            discount_amount = (self.price * self.discount_percent) / 100
            return self.price - discount_amount
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file = models.FileField(upload_to='product_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
