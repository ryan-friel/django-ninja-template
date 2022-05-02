from ninja import Schema, ModelSchema
from .models import Ingredient

class IngredientSchema(ModelSchema):
    class Config:
        model = Ingredient
        model_fields= '__all__'

class NotFoundSchema(Schema):
    message: str