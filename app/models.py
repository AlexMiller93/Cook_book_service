from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    times_cooked = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self) -> str:
        if self.times_cooked:
            return f"{self.id}. {self.name} - cooked {self.times_cooked} times"
        return f"{self.id}. {self.name}"
    
    class Meta:
        ordering = ['id']
        verbose_name = 'product'
        verbose_name_plural = 'products'

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='ProductsInRecipe')
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name}"
    
    class Meta:
        ordering = ['id']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class ProductsInRecipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    
    
