from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from django.shortcuts import redirect

from cars.models import Categories
from cars.models import Products


def q_search(query):

    if query and len(query) >= 2:
        
        vector = SearchVector("category__name", "name", "description")
        query = SearchQuery(query)

        result = (
            Products.objects.annotate(rank=SearchRank(vector, query))
            .filter(rank__gt=0)
            .order_by("-rank")
        )

        result = result.annotate(
            headline_category=SearchHeadline(
                "category__name",
                query,
                start_sel='<span style="background-color: yellow;">',
                stop_sel='</span>',
            )
        )

        result = result.annotate(
            headline_name=SearchHeadline(
                "name",
                query,
                start_sel='<span style="background-color: yellow;">',
                stop_sel='</span>',
            )
        )

        result = result.annotate(
            bodyline=SearchHeadline(
                "description",
                query,
                start_sel='<span style="background-color: yellow;">',
                stop_sel='</span>',
            )
        )

        return result
    
    else:

        return Products.objects.all()
    
def calculate_installment(sell_price, term):
    # Коэффициенты для расчета рассрочки
    coefficients = {
        24: 1.1,
        36: 1.15,
        60: 1.2
    }

    # Рассчитываем рассрочку по формуле: цена * коэффициент / срок
    return round(sell_price * coefficients[term] / term, 2)