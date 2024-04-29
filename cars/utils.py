from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from cars.models import Products


def q_search(query):

    if len(query) >= 2:

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

        return Products.objects.none()

    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #     q_objects |= Q(category__name__icontains=token)

    # return Products.objects.filter(q_objects)
