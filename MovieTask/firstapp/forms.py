
from django import forms
from . models import Film,Topic

class FilmForm(forms.ModelForm):
    class Meta:
        model=Film
        fields=['title','actors','img','desc','date','category','review','rating','url']


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['category']