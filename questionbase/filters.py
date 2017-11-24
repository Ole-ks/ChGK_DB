from .models import Question
import django_filters
from django_filters import filters
from django_filters import widgets
from django import forms
from django.db.models import Q


class MultiFieldSearchFilter(filters.Filter):
    field_class = forms.CharField

    def filter(self, qs, value):
        lookup = self.lookup_expr or 'exact'
        if value in ([], (), {}, None, ''):
            return qs
        if isinstance(self.name, (list, tuple)):
            q = Q()
            for n in self.name:
                q |= Q(**{u'{}__{}'.format(n, lookup): value})
            qs = qs.filter(q)
        else:
            qs = qs.filter(**{u'{}__{}'.format(self.name, lookup): value})
        if self.distinct:
            qs = qs.distinct()
        return qs

class QFilter(django_filters.FilterSet):

    search = MultiFieldSearchFilter(
        name=['qtext', 'answer', 'comment'],
        lookup_expr='icontains',
        label='Искать',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'поиск по вопросу, ответу или комментарию'}))
    author = filters.CharFilter(lookup_expr='icontains', label='Автор',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'поиск по автору'}))

    q_has_img = filters.ChoiceFilter(label='Картинка', widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                      choices=((True, 'есть'),(False, 'нет')))
    q_has_video = filters.ChoiceFilter(label='Видео', widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                      choices=((True, 'есть'),(False, 'нет')))
    q_has_audio = filters.ChoiceFilter(label='Аудио',widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                      choices=((True, 'есть'),(False, 'нет')))
    q_has_media = filters.ChoiceFilter(label='Есть медиа',widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                      choices=((True, 'есть'),(False, 'нет')))
    is_played = filters.ChoiceFilter(widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                     choices=((True, 'да'),(False, 'нет')))
    is_bb = filters.ChoiceFilter(widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                 choices=((True, 'да'), (False, 'нет')))
    wow = filters.ChoiceFilter(widget=forms.Select(attrs={'class': 'btn btn-sm btn-default dropdown-toggle'}),
                               choices=(('WOW', 'WOW'),('-', 'не указано'),('FOO', 'FOO')))
    qtype = filters.ChoiceFilter(label='Тип вопроса', widget=forms.Select(attrs={'class': 'btn btn-sm btn-default dropdown-toggle'}),
                                 choices=(('chgk', 'ЧГК'), ('br', 'Брэйн'), ('tele', 'Теледомик')))
    is_blitz = filters.ChoiceFilter(widget=forms.Select(attrs={'class': 'btn btn-default btn-sm dropdown-toggle'}),
                                 choices=((True, 'да'), (False, 'нет')))
    o = filters.OrderingFilter(
        fields=(('created_date', 'created_date'),),
        field_labels={'created_date': 'дата создания',},
        label='Сортировка',
    )
    class Meta:
        model = Question
        exclude = ['qtext', 'answer', 'altanswer', 'comment', 'source', 'created_date', 'qlink1', 'qlink2', 'qlink3', 'alink1', 'alink2', 'alink3']