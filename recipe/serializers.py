
from accounts.models import Tag,Ingredient,Recipe
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    ''' serialize a recipe '''
    tags = serializers.PrimaryKeyRelatedField(
        many = True,
        
        queryset = Tag.objects.all()
    )

    ingredients = serializers.PrimaryKeyRelatedField(
        many= True,
        
        queryset = Ingredient.objects.all()
    )


    class Meta:
        model = Recipe
        fields = ('id','title','ingredients','tags','time_minutes','price','link')

        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    '''serialzie a recipe detail'''
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags = TagSerializer(many=True,read_only=True)





        