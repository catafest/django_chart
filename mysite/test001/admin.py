from django.contrib import admin
# Register your models here.
from .models import Test001
# https://www.youtube.com/watch?v=g5DTIiFAiSk
from .models import Snippet 

# group 
from django.contrib.auth.models import Group 

from .models import Author, Book 

admin.site.site_header = 'catafest area! '
"""
class SnippetAdmin(admin.ModelAdmin):
    exclude = ('title', )
    fields = ('title', )
    
admin.site.register(Snippet, SnippetAdmin)
"""
#
admin.site.register(Snippet)

# remove 

# register to admin area 
admin.site.register(Test001)
#
admin.site.register(Author)
admin.site.register(Book)

# unregister 
admin.site.unregister(Group)

