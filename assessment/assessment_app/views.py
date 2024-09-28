from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from assessment_app.models import FoodFoodType, Ingredient, IntakeTime, Recipe
from assessment_app.serializer import FoodFoodTypeModelSerializer, IngredientModelSerializer, IntakeTimeModelSerializer, RecipeModelSerializer


# Create your views here.


class recipeModelViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer

# class ingredientRecipeModelViewSet(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientModelSerializer

class ingredientRecipeModelViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.order_by("name")
    serializer_class = IngredientModelSerializer

class createIngredientViewSet(viewsets.ViewSet):
    
    def create(self, request):
        data = request.data
        if type(data) is dict:
            responseSerializer = IngredientModelSerializer(data=data)
        else:
            responseSerializer = IngredientModelSerializer(data=data, many=True)
        if responseSerializer.is_valid()==True:
            responseSerializer.save()
            return Response(responseSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(responseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodTypeIntakeTimeListView(APIView):
    def get(self, request):
        food_type_name = request.query_params.get('food_type_name', None)
        if food_type_name:
            food_types = FoodFoodType.objects.filter(food_type_name__icontains=food_type_name)
        else:
            food_types = FoodFoodType.objects.all()
        
        intake_time_name = request.query_params.get('intake_time', None)
        if intake_time_name:
            intake_times = IntakeTime.objects.filter(intake_time__icontains=intake_time_name)
        else:
            intake_times = IntakeTime.objects.all()

        food_types_serializer = FoodFoodTypeModelSerializer(food_types, many=True).data
        intake_times_serializer = IntakeTimeModelSerializer(intake_times, many=True).data

        return Response({
            'food_types': food_types_serializer,
            'intake_times': intake_times_serializer
        })