from django.contrib import admin
from app.models import Product, Recipe, ProductsInRecipe


class ProductsInRecipeInline(admin.TabularInline):
    model = ProductsInRecipe
    extra = 1
    
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = (ProductsInRecipeInline, )


admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
