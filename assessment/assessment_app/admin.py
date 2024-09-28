from django.contrib import admin
from assessment_app.models import FoodFoodType, Ingredient, IntakeTime, Recipe

# Register your models here.

admin.site.register(FoodFoodType)
admin.site.register(Ingredient)
admin.site.register(IntakeTime)
admin.site.register(Recipe)
