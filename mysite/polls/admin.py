from django.contrib import admin


from .models import Question
from .models import Choice

# Choice objects are edited on the Question admin page. 
# By default, provide enough fields for 3 choices.
# admin.StackedInline
# admin.TabularInline: tabular way of displaying inline related objects
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # reordering the fields on the edit form
    # fields = ['pub_date', 'question_text', 'quation_details']
    
    # you might want to split the form up into fieldsets
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    
    # By default, Django displays the str() of each object. But sometimes it’d 
    # be more helpful if we could display individual fields. To do that, use the 
    # list_display admin option, which is a tuple of field names to display, 
    # as columns, on the change list page for the object
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # adds a “Filter” sidebar that lets people filter the change list by the
    # pub_date field:
    list_filter = ['pub_date']
    
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text', 'quation_details', 'question_type']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    # Adding related objects
    # a Question has multiple Choices, and the admin page doesn’t display choices.
    # There are two ways to solve this problem. 
    # The first is to register Choice with the admin like: admin.site.register(Choice)
    # It’d be better if you could add a bunch of Choices directly when you create 
    # the Question object.
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
