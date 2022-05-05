from django.contrib import admin

from main.models import Question, Category


class QuestionAdmin(admin.ModelAdmin):
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
    readonly_fields = ["airdate", "created_at", "updated_at"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["title", "created_at", "updated_at", "clues_count"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
