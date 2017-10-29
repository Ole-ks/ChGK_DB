from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Question
from .forms import QuestForm
from .filters import QFilter


@login_required
def question_list(request):
    # If user choose sorting order
    orderby = request.GET.get('sort', False)
    if orderby in ['new', 'old', 'np']:
        request.session['orderby'] = orderby
    # sort queryset
    if 'orderby' in request.session:
        if request.session['orderby'] == 'new':
            questions = Question.objects.order_by('-created_date')
        elif request.session['orderby'] == 'old':
            questions = Question.objects.order_by('created_date')
        elif request.session['orderby'] == 'np':
            questions = Question.objects.order_by('is_played', '-created_date')
    else:
        questions = Question.objects.order_by('-created_date')
    # Paginator parameter
    q_per_page = int(request.GET.get('cou', False))
    if q_per_page in [10, 20, 50]:
        request.session['q_per_page'] = q_per_page

    if 'q_per_page' in request.session:
        paginator = Paginator(questions, request.session['q_per_page'])
    else:
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
            quest.qtextlower = quest.qtext.lower()
            quest.created_date = timezone.now()
            quest.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
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
            quest.qtextlower = quest.qtext.lower()
            quest.answerlower = quest.answer.lower()
            quest.commentlower = quest.comment.lower()
            quest.created_date = timezone.now()
            quest.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
                return redirect('quest_list')
    else:
        form = QuestForm(instance=quest)
    return render(request, 'questionbase/quest_edit.html', {'form': form})


@login_required
def search(request):
    quest_search = Question.objects.all()
    quest_filter = QFilter(request.GET, queryset=quest_search)
    return render(request, 'questionbase/quest_search.html', {'filter': quest_filter})


@login_required
def quest_remove(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    quest.delete()
    return redirect('quest_list')