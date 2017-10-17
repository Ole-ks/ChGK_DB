from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Question
from .forms import QuestForm


def question_list(request):
    questions = Question.objects.order_by('-created_date')
    return render(request, 'questionbase/quest_list.html', {'questions': questions})

def quest_detail(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    return render(request, 'questionbase/quest_detail.html', {'quest': quest})

def quest_new(request):
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_date = timezone.now()


            quest.save()
            return redirect('quest_detail', pk=quest.pk)
    else:
        form = QuestForm(request.POST)
    return render(request, 'questionbase/quest_edit.html', {'form': form})

def quest_edit(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestForm(request.POST, request.FILES, instance=quest)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_date = timezone.now()
            quest.save()
            return redirect('quest_detail', pk=quest.pk)
    else:
        form = QuestForm(instance=quest)
    return render(request, 'questionbase/quest_edit.html', {'form': form})

