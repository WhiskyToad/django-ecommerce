from typing import List

import strawberry

from .types import Fruit


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
