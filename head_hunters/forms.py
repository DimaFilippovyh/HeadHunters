from django import forms
from .models import Topic, Summary, Vacancy


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'name': ''}


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['text', 'photo']
        labels = {'text': 'Summary:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['text']
        labels = {'text': 'Vacancy:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
