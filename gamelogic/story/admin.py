from django.contrib import admin
from story.models import Story, Question
    
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('key',)}
    list_display = ('title', 'editorial_alpha', 'science_alpha', 'editorial_beta', 'science_beta', 'editorial_gold', 'science_gold',)
    list_editable = ('editorial_alpha', 'science_alpha', 'editorial_beta', 'science_beta', 'editorial_gold', 'science_gold',)
    list_filter = ('key','title', 'modified', 'editorial_alpha', 'science_alpha', 'editorial_beta', 'science_beta', 'editorial_gold', 'science_gold',)
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','story_question_appears_on', 'story_question_answer_goes_to',)
    list_filter = ('story_question_appears_on', 'story_question_answer_goes_to',)
    
admin.site.register(Story, StoryAdmin)
admin.site.register(Question, QuestionAdmin)