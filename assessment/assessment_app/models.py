from django.db import models

# Create your models here.

class FoodFoodType(models.Model):
    
    """
    To store information about FoodFoodType
    """

    food_type_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.food_type_name


class Ingredient(models.Model):

    """
    To store information about Ingredient
    """

    name = models.CharField(max_length=200)
    FoodType = models.ForeignKey(FoodFoodType, related_name="Food_Type", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class IntakeTime(models.Model):

    """
    To store information about IntakeTime
    """

    intake_time = models.CharField(max_length=200)
    
    def __str__(self):
        return self.intake_time


class Recipe(models.Model):

    """
    To store information about Recipe
    """

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, related_name="receipe_ingredients")
    best_suitable = models.ForeignKey(IntakeTime, related_name="receipe_best_suitable", on_delete=models.CASCADE)
    directions = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name