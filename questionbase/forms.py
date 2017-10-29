from django import forms
from .models import Question


class QuestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('qtext',
                  'qlink1',
                  'qlink2',
                  'qlink3',
                  'answer',
                  'altanswer',
                  'alink1',
                  'alink2',
                  'alink3',
                  'comment',
                  'author',
                  'source',
                  'is_played',
                  'is_bb',)
        widgets = {
            'qtext': forms.Textarea(attrs={'class': 'form-control'}),
            'qlink1': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'qlink2': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'qlink3': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
            'altanswer': forms.TextInput(attrs={'class': 'form-control'}),
            'alink1': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'alink2': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'alink3': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'is_played': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'is_bb': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
        }
