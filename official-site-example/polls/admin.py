from django.contrib import admin

# Register your models here.
from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ['pub_date','question_text','was_published_resently']
    inlines = [ChoiceInline]



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
