from django import forms
from .models import Question, Choice

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'date'
        ]

class CreateChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = [
            'question',
            'choice_text',
            'votes'
        ]