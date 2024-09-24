from django import forms

from . models import Topic, Entry

class TopicForm(forms.ModelForm):
    """a form to hold topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    """A form to hold entry"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = { 'text' : ''}
        widgets = { 'text' : forms.Textarea(attrs={ 'cols' : 80})}