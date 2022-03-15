from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Summary, Vacancy
from .forms import TopicForm, SummaryForm, VacancyForm
from .check_of_validation import check_topic_owner


def index(request):
    return render(request, 'head_hunters/index.html')


@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}
    return render(request, 'head_hunters/topics.html', context=context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.user.profile.is_employee:
        summaries = topic.summary_set.order_by('date_added')
        vacancies = topic.vacancy_set.filter(owner=request.user)\
            .order_by('date_added')
        request_for = 'head_hunters/topic_for_employee.html'
    else:
        summaries = topic.summary_set.filter(owner=request.user)\
            .order_by('date_added')
        vacancies = topic.vacancy_set.order_by('date_added')
        request_for = 'head_hunters/topic_for_individual.html'

    context = {'topic': topic, 'summaries': summaries, 'vacancies': vacancies}
    return render(request, request_for, context=context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('head_hunters:topics')

    context = {'form': form}
    return render(request, 'head_hunters/new_topic.html', context=context)


@login_required
def new_summary(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = SummaryForm()
    else:
        form = SummaryForm(data=request.POST)
        if form.is_valid():
            new_summary = form.save(commit=False)
            new_summary.topic = topic
            new_summary.owner = request.user
            new_summary.save()
            return redirect('head_hunters:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'head_hunters/new_summary.html', context=context)


@login_required
def edit_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    topic = summary.topic

    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = SummaryForm(instance=summary)
    else:
        form = SummaryForm(instance=summary, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('head_hunters:topic', topic_id=topic.id)

    context = {'summary': summary, 'topic': topic, 'form': form}
    return render(request, 'head_hunters/edit_summary.html', context=context)


@login_required
def new_vacancy(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = VacancyForm()
    else:
        form = VacancyForm(data=request.POST)
        if form.is_valid():
            new_vacancy = form.save(commit=False)
            new_vacancy.topic = topic
            new_vacancy.owner = request.user
            new_vacancy.save()
            return redirect('head_hunters:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'head_hunters/new_vacancy.html', context=context)


@login_required
def edit_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    topic = vacancy.topic

    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = VacancyForm(instance=vacancy)
    else:
        form = VacancyForm(instance=vacancy, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('head_hunters:topic', topic_id=topic.id)

    context = {'vacancy': vacancy, 'topic': topic, 'form': form}
    return render(request, 'head_hunters/edit_vacancy.html', context=context)
