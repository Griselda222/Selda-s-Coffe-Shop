from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,null=True,blank=True)
    category_image = models.ImageField(upload_to="category/" ,null=True,blank=True)
    def __str__(self):
        return f"{self.category_name}"
    
class Product(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=True)
    product_image = models.ImageField(upload_to="product/" ,null=True,blank=True)
    # Many to one (One to many)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f"{self.product_name}"

class Factory(models.Model):
    fac_name=models.CharField(max_length=100,null=True,blank=True)
    fac_description=models.TextField(max_length=500,null=True,blank=True)
    fac_image=models.ImageField(upload_to="factory/",null=True,blank=True)
    fac_prize=models.FloatField(max_length=20,null=True,blank=True)

class Contact(models.Model):
    contact_name=models.CharField(max_length=50,null=True,blank=True)
    contact_surname=models.CharField(max_length=50,null=True,blank=True)
    contact_email=models.EmailField(null=True,blank=True)
    contact_comment=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return f"{self.contact_name}{self.contact_surname}"