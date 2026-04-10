from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]})
    ]

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question & Choices", {"fields": ["question", "choice_text"]}),
        ("Vote", {"fields": ["votes"]})
    ]

admin.site.register(Choice,ChoiceAdmin)
