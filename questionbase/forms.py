from django import forms
from .models import Question
from .models import Package


class PkgForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
                  'is_blitz',
                  'is_played',
                  'is_bb',
                  'qtype',
                  'wow',)
        widgets = {
            'qtext': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
            'qlink1': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'qlink2': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'qlink3': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'altanswer': forms.TextInput(attrs={'class': 'form-control'}),
            'alink1': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'alink2': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'alink3': forms.ClearableFileInput(attrs={'class': 'filestyle', 'data-icon': 'false', 'data-buttonBefore': 'true', 'data-size': 'sm'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'is_blitz': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'is_played': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'is_bb': forms.CheckboxInput(attrs={'class': 'checkbox', 'style': 'width: 30px'}),
            'qtype': forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
            'wow': forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
        }