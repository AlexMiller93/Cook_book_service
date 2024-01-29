from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    times_cooked = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.name} - cooked {self.times_cooked} times"

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='ProductsInRecipe')
    
    def __str__(self) -> str:
        return f"{self.name}"

class ProductsInRecipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()
    
