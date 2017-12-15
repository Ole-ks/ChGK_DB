from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Question
from .models import Blitz
from .models import Package
from .models import PackageDetail
from .forms import QuestForm
from .forms import BlitzQuestForm
from .forms import QuestFormForBlitz
from .forms import PkgForm
from .filters import QFilter


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('search')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def quest_new(request):
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        if form.is_valid():
            quest = form.save(commit=False)
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
                pfrom = request.GET.get('from', None)
                if pfrom:
                    return redirect(pfrom)
                return redirect('search')
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
                pfrom = request.GET.get('from', None)
                if pfrom:
                    return redirect(pfrom + '#q' + pk)
                return redirect('search')
    else:
        form = QuestForm(instance=quest)
    return render(request, 'questionbase/quest_edit.html', {'form': form, 'questid': pk})


@login_required
def blitz_quest_new(request):
    if request.method == 'POST':
        qform = QuestFormForBlitz(request.POST, request.FILES)
        bform = BlitzQuestForm(request.POST)
        if all((qform.is_valid(), bform.is_valid())):
            quest = qform.save(commit=False)
            quest.q_has_media = quest.has_media()
            quest.q_has_img = quest.has_img()
            quest.q_has_video = quest.has_video()
            quest.q_has_audio = quest.has_audio()
            quest.created_date = timezone.now()
            quest.is_blitz = True
            quest.save()
            bquest = bform.save(commit=False)
            bquest.question = quest
            bquest.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
                pfrom = request.GET.get('from', None)
                if pfrom:
                    return redirect(pfrom)
                return redirect('search')
    else:
        qform = QuestFormForBlitz(request.POST)
        bform = BlitzQuestForm(request.POST)
    return render(request, 'questionbase/blitz_quest_edit.html', {'qform': qform, 'bform': bform})


@login_required
def blitz_quest_edit(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    blitz = get_object_or_404(Blitz, question=pk)
    if request.method == "POST":
        qform = QuestFormForBlitz(request.POST, request.FILES, instance=quest)
        bform = BlitzQuestForm(request.POST, instance=blitz)
        if qform.is_valid():
            quest = qform.save(commit=False)
            quest.q_has_media = quest.has_media()
            quest.q_has_img = quest.has_img()
            quest.q_has_video = quest.has_video()
            quest.q_has_audio = quest.has_audio()
            quest.save()
            bform.save()
            if 'submit_new' in request.POST:
                return redirect('quest_new')
            elif 'submit_edit' in request.POST:
                return redirect('quest_edit', pk=quest.pk)
            else:
                pfrom = request.GET.get('from', None)
                if pfrom:
                    return redirect(pfrom + '#q' + pk)
                return redirect('search')
    else:
        qform = QuestFormForBlitz(instance=quest)
        bform = BlitzQuestForm(instance=blitz)
    return render(request, 'questionbase/blitz_quest_edit.html', {'qform': qform, 'bform': bform, 'questid': pk})


@login_required
def search(request):
    quest_filter = QFilter(request.GET, queryset=Question.objects.filter(is_deleted=False).order_by('-created_date'))
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

    q_in_pkg_list = []
    if 'work_pkg_id' in request.session:
        q_in_pkg_list = PackageDetail.objects.filter(pkg_id=request.session['work_pkg_id']).values_list('quest_id', flat=True)

    return render(request, 'questionbase/quest_search.html', {'filter': quest_filter, 'questions': questions, 'current_path': request.get_full_path(), 'q_in_pkg_list': q_in_pkg_list})


@login_required
def pkg_new(request):
    if request.method == 'POST':
        form = PkgForm(request.POST)
        if form.is_valid():
            pkg = form.save(commit=False)
            pkg.created_date = timezone.now()
            pkg.save()
            request.session['work_pkg_id'] = pkg.id
            request.session['work_pkg_name'] = pkg.name
            return redirect('search')
    else:
        form = PkgForm(request.POST)
    return render(request, 'questionbase/pkg_new.html', {'form': form, 'current_path': request.get_full_path()})


@login_required
def pkg_list(request):
    pkgs = Package.objects.order_by('-created_date')

    # Paginator parameter
    q_per_page = int(request.GET.get('cou', False))
    if q_per_page in [1, 10, 20, 50]:
        request.session['q_per_page'] = q_per_page

    if 'q_per_page' in request.session:
        paginator = Paginator(pkgs, request.session['q_per_page'])
    else:
        paginator = Paginator(pkgs, 10)
    page = request.GET.get('page')
    try:
        pkgs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pkgs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pkgs = paginator.page(paginator.num_pages)

    return render(request, 'questionbase/pkg_list.html', {'pkgs': pkgs, 'current_path': request.get_full_path()})


@login_required
def pkg_detail(request, pk):
    pkg = get_object_or_404(Package, pk=pk)
    questions = Question.objects.filter(question_in_pkg__pkg_id=pk)
    request.session['work_pkg_id'] = pkg.id
    request.session['work_pkg_name'] = pkg.name
    return render(request, 'questionbase/pkg_detail.html', {'questions': questions, 'current_path': request.get_full_path()})


@login_required
def search_w_a(request):
    request.session['with_answers'] = 'True'
    pfrom = request.GET.get('from', None)
    if pfrom:
        return redirect(pfrom)
    return redirect('search')


@login_required
def search_n_a(request):
    request.session['with_answers'] = 'False'
    pfrom = request.GET.get('from', None)
    if pfrom:
        return redirect(pfrom)
    return redirect('search')


@login_required
def quest_remove(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    quest.is_deleted = True
    quest.save()
    return redirect('search')


@login_required
def quest_restore(request, pk):
    quest = get_object_or_404(Question, pk=pk)
    quest.is_deleted = False
    quest.save()
    return redirect('search')


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

    return render(request, 'questionbase/deleted.html', {'questions': questions, 'current_path': request.get_full_path()})

@login_required
def add_quest_to_pkg(request):
    q_id = request.GET.get('q_id', None)
    if q_id:
        quest = get_object_or_404(Question, pk=q_id)
        pkg = get_object_or_404(Package, pk=request.session['work_pkg_id'])
        p = PackageDetail(quest_id=quest, pkg_id=pkg)
        p.save()
        data = {
            'cou': 'Added!'
        }
    return JsonResponse(data)