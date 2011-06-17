from django.contrib import admin
from story.models import Story
    
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('key')}

admin.site.register(Story, StoryAdmin)