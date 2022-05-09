import requests
from rest_framework import (
    permissions,
    generics,
    status,
    response,
)

from main.serializers import QuestionSerializer
from main.models import Question, Category


class QuestionView(generics.ListAPIView):
    """
    API endpoint that allows Questions to be viewed or requested from external site.
    """
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        last_question = Question.objects.order_by("internal_id").last()

        count_str = request.data.get("questions_num")
        if count_str is None:
            count_str = request.query_params.get("questions_num")
        count = int(count_str)

        while count > 0:
            site_response = requests.get(
                url="http://jservice.io/api/random",
                params={"count": count},
            )
            result = site_response.json()
            for record in result:
                category_record = record.pop("category")
                category, created = Category.objects.get_or_create(
                    id=category_record["id"], defaults=category_record
                )
                external_id = record.get("id")
                if Question.objects.filter(id=external_id).exists():
                    continue
                serializer = QuestionSerializer(data=record)
                if serializer.is_valid():
                    question = serializer.save()
                    question.category = category
                    question.save()
                    count -= 1

        serializer = QuestionSerializer(last_question)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
