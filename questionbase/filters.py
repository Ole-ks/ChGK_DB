from .models import Question
import django_filters
from django import forms


class QFilter(django_filters.FilterSet):
    iquery = Question.objects.values_list('author', flat=True).distinct().order_by('author')
    iquery_choices = [('', 'None')] + [(id, id) for id in iquery]
    author = django_filters.ChoiceFilter(choices=iquery_choices)

    class Meta:
        model = Question
        fields = {
            'qtextlower': ['icontains'],
            'answerlower': ['icontains'],
            'commentlower': ['icontains'],
            'author': ['icontains'],
            'is_played': ['exact'],
            'is_bb': ['exact'],
        }
