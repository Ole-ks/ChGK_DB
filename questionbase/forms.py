from django import forms
from .models import Question

class QuestForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('qtext',
                  'answer',
                  'altanswer',
                  'comment',
                  'author',
                  'source',
                  'is_played',
                  'is_bb',
                  'qlink1',
                  'qlink2',
                  'qlink3',
                  'alink1',
                  'alink2',
                  'alink3',)
        widgets = {
            'qtext': forms.Textarea(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
            'altanswer': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'is_played': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'is_bb': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'qlink1': forms.ClearableFileInput(attrs={'class': 'form-control', 'data-text': '123'}),
            'qlink2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'qlink3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'alink1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'alink2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'alink3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
