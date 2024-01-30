from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from app.models import Product, Recipe, ProductsInRecipe

# Create your views here.

def add_product_to_recipe(request):
    
    # add_product_to_recipe 
    # с параметрами recipe_id, product_id, weight. 
    # Функция добавляет к указанному рецепту указанный продукт 
    # с указанным весом. 
    # Если в рецепте уже есть такой продукт, 
    # то функция должна поменять его вес в этом рецепте на указанный.
    
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    
    # handle possible exceptions 
    if not (recipe_id and product_id and weight):
        raise Http404("All required parameters are not specified.")
    try:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)
        
    except (Recipe.DoesNotExist, Product.DoesNotExist):
        raise Http404("The specified recipe or product was not found.")
    
    # add products to recipe
    product_in_recipe, created = ProductsInRecipe.objects.get_or_create(
        recipe=recipe, product=product, defaults={"weight": weight})
    
    #  update product weight if it was in recipe
    if not created:
        product_in_recipe.weight = weight
        product_in_recipe.save()
    
    return HttpResponse("Product added to recipe successfully")

def cook_recipe(request):
    '''
    cook_recipe c параметром recipe_id. 
    Функция увеличивает на единицу количество приготовленных блюд 
    для каждого продукта, входящего в указанный рецепт.
    '''
    
    recipe_id = request.GET.get('recipe_id')
    
    # handle possible exceptions 
    if not recipe_id:
        raise Http404("Required parameter recipe_id is not specified.")
    try:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
    except Recipe.DoesNotExist:
        raise Http404("The specified recipe was not found.")
    
    for product in recipe.products.all():
        product.times_cooked += 1
        product.save()

    return HttpResponse("Recipe cooked successfully")

def show_recipes_without_product(request):
    '''
    show_recipes_without_product с параметром product_id. 
    Функция возвращает HTML страницу, на которой размещена таблица. 
    В таблице отображены id и названия всех рецептов, 
    в которых указанный продукт отсутствует, или присутствует 
    в количестве меньше 10 грамм. Страница должна генерироваться 
    с использованием Django templates
    '''
    
    product_id = request.GET.get('product_id')
    
    if not product_id:
        raise Http404("Required parameter product_id is not specified.")
    try:
        product = get_object_or_404(Product, id=product_id)
        
    except Product.DoesNotExist:
        raise Http404("The specified product was not found.")
    
    
    recipes = Recipe.objects.exclude(
        productsinrecipe__product=product, productsinrecipe__weight__gte=10
        )

    context = {'recipes': recipes}
    
    return render(request, 'recipes_without_product.html', context)
    
