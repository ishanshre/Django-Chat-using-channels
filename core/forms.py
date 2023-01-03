from django import forms

from core.models import Message

class ChatBodyMessage(forms.ModelForm):
    body = forms.CharFieldbody = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows":3, "placeholder": "Type message here",}))
    class Meta:
        model = Message
        fields = ['body']
        labels ={
            "body":""
        }