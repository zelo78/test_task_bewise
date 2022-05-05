from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "answer",
            "question",
            "value",
            "airdate",
            "created_at",
            "updated_at",
            "category",
        ]
        depth = 1
