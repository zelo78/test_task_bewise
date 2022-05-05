from django.urls import path
from .views import QuestionView

urlpatterns = [
    path("questions/", QuestionView.as_view(), name="questions"),
]
