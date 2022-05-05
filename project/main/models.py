from django.db import models
from django.utils import timezone


class Question(models.Model):
    internal_id = models.BigAutoField(primary_key=True)
    id = models.PositiveIntegerField("ID", unique=True)
    answer = models.CharField("ответ", max_length=128)
    question = models.TextField("вопрос")
    value = models.PositiveIntegerField("стоимость", null=True)
    airdate = models.DateTimeField("дата эфира", null=True)
    created_at = models.DateTimeField("дата создания", null=True)
    updated_at = models.DateTimeField("дата обновления", null=True)
    category = models.ForeignKey(
        "Category", verbose_name="категория", on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return f"Вопрос #{self.id}: {self.question:.20s}. Ответ: {self.answer:.20s}"


class Category(models.Model):
    internal_id = models.BigAutoField(primary_key=True)
    id = models.PositiveIntegerField("ID", unique=True)
    title = models.CharField("наименование", max_length=128)
    created_at = models.DateTimeField("создана", default=timezone.now)
    updated_at = models.DateTimeField("обновлена", default=timezone.now)
    clues_count = models.PositiveIntegerField("количество ключей")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f"Категория #{self.id}: {self.title}"
