from django.contrib import admin
from .models import Question, Answer
# Register your models here.

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author', 'created_at', 'deleted']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'content', 'author', 'created_at', 'upvotes', 'downvotes']