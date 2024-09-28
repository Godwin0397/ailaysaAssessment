from django.urls import path, include
from assessment_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'routerModelViewSetRecipe', views.recipeModelViewSet, basename='router-modelviewset-recipe')
router.register(r'routerModelViewSetIngredientRecipe', views.ingredientRecipeModelViewSet, basename='router-modelviewset-ingredient-recipe')
router.register(r'routerCreateIngredientViewSet', views.createIngredientViewSet, basename='router-create-ingredient')



urlpatterns = [
    path('food-intake/', views.FoodTypeIntakeTimeListView.as_view(), name='food-intake-list'),
    path('', include(router.urls)),
]