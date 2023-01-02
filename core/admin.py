from django.contrib import admin
from core.models import Message, Friend
# Register your models here.


admin.site.register(Friend)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender','receiver','body']
    
