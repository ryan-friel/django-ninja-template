from distutils.util import rfc822_escape
from typing import List, Optional
from ninja import NinjaAPI
from .models import Ingredient
from .schema import IngredientSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/")
def test(request):
    return {"Response": "Successfully hit the gainful endpoint!"}


@api.get("/ingredients", response={200: List[IngredientSchema]})
def get_all_ingredients(request, name: Optional[str] = None):
    if name:
        return Ingredient.objects.filter(name=name)

    return Ingredient.objects.all()


@api.get("/ingredients/{name}", response={200: IngredientSchema, 404: NotFoundSchema})
def get_all_ingredients(request, name: str):
    output: list = Ingredient.objects.filter(name=name)
    # The output as a list will return true if there are values available.
    if output:
        output = output[0]
        return 200, output

    else:
        return 404, {"message": f'The name {name} does not exist'}


@api.post("/ingredients", response={201: IngredientSchema})
def create_ingredient(request, ingredient: IngredientSchema):
    output = Ingredient.objects.create(**ingredient.dict())
    return 201, output


@api.put("/ingredients/{name}", response={200: IngredientSchema, 404: NotFoundSchema})
def update_ingredient(request, name: str, data: IngredientSchema):
    found_ingredient = Ingredient.objects.filter(name=name)
    # The output as a list will return true if there are values available.

    if found_ingredient:

        found_ingredient.update(**data.dict())
        return 200, found_ingredient[0]

    else:
        return 404, {"message": f'The name {name} does not exist'}


# I'm not sure which I prefer more for put operator.
@api.put("/ingredients", response={200: IngredientSchema, 404: NotFoundSchema})
def update_ingredient(request, data: IngredientSchema):
    name: str = data.dict()['name']
    found_ingredient = Ingredient.objects.filter(name=name)

    # The output as a list will return true if there are values available.
    if found_ingredient:

        found_ingredient.update(**data.dict())
        return 200, found_ingredient[0]

    else:
        return 404, {"message": f'The name {name} does not exist'}


@api.delete("/ingredients/{name}", response={200: None, 404: NotFoundSchema})
def delete_ingredient(request, name: str):
    found_ingredient = Ingredient.objects.filter(name=name)
    if found_ingredient:
        found_ingredient = found_ingredient[0]
        found_ingredient.delete()
        return 200

    else:
        return 404, {"message": f'The name {name} does not exist'}
