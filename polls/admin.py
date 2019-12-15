from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    # Changing Order of fields :
    #       fields = ['question_text', 'pub_date']
    # Grouping fields in sections, it should looks more pretty:
    fieldsets = [
        ( 'Question descpription', { 'fields': ['question_text'] } ),
        ( 'Date information', { 'fields': ['pub_date'] } ),
    ]
    # Displaying list of related objects
    inlines = [ChoiceInline]
    # List of columns of Question list page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Standtart simply filters for some columns
    list_filter = ['pub_date']
    # Search widget for some fields, in our case for Question's text
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
