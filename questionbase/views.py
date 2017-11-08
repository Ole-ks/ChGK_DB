from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils import timezone
from .models import Question
from .forms import QuestForm
from .filters import QFilter


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            #return redirect('change_password')
            response = redirect('search')
            if 'search_query' in request.session:
                response['Location'] += '?' + request.session['search_query']
            return response
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def to_full_form(request):
    response = redirect('search')
    if 'search_query' in request.session:
        response['Location'] += '?' + request.session['search_query']
    return response


@login_required
def to_empty_form(request):
    request.session['search_query'] = ''
    return redirect('search')


@login_required
def quest_new(request):
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.qtextlower = quest.qtext.lower()
            quest.answerlower = quest.answer.lower()
            quest.commentlower = quest.comment.lower()
            quest.q_has_media = quest.has_media()
            quest.q_has_img = quest.has_img()
            quest.q_has_video = quest.has_video()
            quest.q_has_audio = quest.has_audio()
            quest.created_date = timezone.now()
            quest.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
                #return redirect('search')
                response = redirect('search')
                if 'search_query' in request.session:
                    response['Location'] += '?' + request.session['search_query']
                return response
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
            quest.q_has_media = quest.has_media()
            quest.q_has_img = quest.has_img()
            quest.q_has_video = quest.has_video()
            quest.q_has_audio = quest.has_audio()
            quest.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
                #return redirect('search')
                response = redirect('search')
                if 'search_query' in request.session:
                    response['Location'] += '?' + request.session['search_query']
                return response
    else:
        form = QuestForm(instance=quest)
    return render(request, 'questionbase/quest_edit.html', {'form': form})


@login_required
def search(request):
    quest_filter = QFilter(request.GET, queryset=Question.objects.filter(is_deleted=False))
    questions = quest_filter.qs

    if 'find-btn' in request.GET:
        request_dict = dict(request.GET)
        del request_dict['find-btn']
        request_dict_url = ''
        for key, value in request_dict.items():
            request_dict_url = request_dict_url + '&' + str(key) + '=' + str(value)[2:-2]
        request.session['search_query'] = request_dict_url
    if 'cancel-btn' in request.GET:
        request.session['search_query'] = ''
    # Paginator parameter
    q_per_page = int(request.GET.get('cou', False))
    if q_per_page in [1, 10, 20, 50]:
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

    return render(request, 'questionbase/quest_search.html', {'filter': quest_filter, 'questions': questions})


@login_required
def quest_remove(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    quest.is_deleted = True
    quest.save()
    #return redirect('search')
    response = redirect('search')
    if 'search_query' in request.session:
        response['Location'] += '?' + request.session['search_query']
    return response


@login_required
def quest_restore(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    quest.is_deleted = False
    quest.save()
    #return redirect('search')
    response = redirect('search')
    if 'search_query' in request.session:
        response['Location'] += '?' + request.session['search_query']
    return response


@login_required
def delete_forever(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    for file in [quest.qlink1, quest.qlink2, quest.qlink3, quest.alink1, quest.alink2, quest.alink3]:
        try:
            file.delete()
            quest.save()
        except:
            print('-------something went wrong++++++++++++++++++++++++++++++++++++++++++++')
    quest.delete()
    return redirect('deleted')


@login_required
def deleted(request):
    questions = Question.objects.filter(is_deleted=True).order_by('-created_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 5)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questionbase/deleted.html', {'questions': questions})