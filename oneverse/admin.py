#coding: utf-8
from django.contrib import admin
from models import Verse



# a class to customize admin the models
class VerseAdmin(admin.ModelAdmin):
    #field display on change list in admin exchard
    fields = ("push_date",'verse', 'source')


admin.site.register(Verse, VerseAdmin)
