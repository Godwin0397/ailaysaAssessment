from rest_framework import serializers
from assessment_app.models import FoodFoodType, Ingredient, IntakeTime, Recipe

class IntakeTimeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntakeTime
        fields = ['id', 'intake_time']
        extra_kwargs = {'id': {'read_only': True}}

class RecipeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients', 'best_suitable', 'directions']
        extra_kwargs = {'id': {'read_only': True}}
    
    def to_internal_value(self, data):
        data['directions'] = 'Direction for ' + data['name']
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['name'] = ret['name'] + ' Good For Health'
        return ret

class IngredientModelSerializer(serializers.ModelSerializer):

    recipe = RecipeModelSerializer(source="receipe_ingredients", many=True, read_only=True)

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'FoodType', 'recipe']
        extra_kwargs = {'id': {'read_only': True}}


class FoodFoodTypeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodFoodType
        fields = ['id', 'food_type_name']
        extra_kwargs = {'id': {'read_only': True}}



