# types.py
from typing import List

import strawberry
from strawberry import auto

from . import models


@strawberry.django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: "Color"


@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: List[Fruit]
