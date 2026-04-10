from django.contrib import admin
from polls.models import Question, Choice

class ChoiceTabularInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    inlines = [ChoiceTabularInline]

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question & Choices", {"fields": ["question", "choice_text"]}),
        ("Vote", {"fields": ["votes"]})
    ]

admin.site.register(Choice,ChoiceAdmin)
