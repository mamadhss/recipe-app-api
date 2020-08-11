from rest_framework import viewsets,mixins
from accounts.models import Tag,Ingredient,Recipe
from rest_framework import serializers
from rest_framework import permissions
from .serializers import TagSerializer,IngredientSerializer,RecipeSerializer,RecipeDetailSerializer



class TagViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):

   
    serializer_class = TagSerializer

    queryset = Tag.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self,serializer):
        ''' create new tag '''

        serializer.save(user=self.request.user)  

class IngredientViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()       

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')      

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)            



class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return RecipeDetailSerializer
        return self.serializer_class 

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)       

    
         