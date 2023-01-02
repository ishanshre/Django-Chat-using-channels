from django.contrib import admin
from core.models import Message
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender','receiver','body']
    
