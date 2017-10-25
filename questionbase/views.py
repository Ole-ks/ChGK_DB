from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Question
from .forms import QuestForm

@login_required
def question_list(request):
    questions = Question.objects.order_by('-created_date')
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questionbase/quest_list.html', {'questions': questions})

@login_required
def quest_detail(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    return render(request, 'questionbase/quest_detail.html', {'quest': quest})

@login_required
def quest_new(request):
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_date = timezone.now()
            quest.save()
            return redirect('quest_list')
    else:
        form = QuestForm(request.POST)
    return render(request, 'questionbase/quest_edit.html', {'form': form})

@login_required
def quest_edit(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestForm(request.POST, request.FILES, instance=quest)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_date = timezone.now()
            quest.save()
            return redirect('quest_list')
    else:
        form = QuestForm(instance=quest)
    return render(request, 'questionbase/quest_edit.html', {'form': form})

