from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Summary, Vacancy
from users.models import Profile
from .forms import TopicForm, SummaryForm, VacancyForm
from .check_of_validation import check_object_owner


def index(request):
    return render(request, 'head_hunters/index.html')


@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}
    return render(request, 'head_hunters/topics.html', context=context)


@login_required
def topic(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
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
def new_summary(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    if request.method != 'POST':
        form = SummaryForm()
    else:
        form = SummaryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_summary = form.save(commit=False)
            new_summary.topic = topic
            new_summary.owner = request.user
            new_summary.save()
            return redirect('head_hunters:topic', topic_slug=topic_slug)

    context = {'topic': topic, 'form': form}
    return render(request, 'head_hunters/new_summary.html', context=context)


@login_required
def edit_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    topic = summary.topic

    check_object_owner(summary, request)

    if request.method != 'POST':
        form = SummaryForm(instance=summary)
    else:
        form = SummaryForm(instance=summary, data=request.POST,
            files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('head_hunters:topic', topic_slug=topic.slug)

    context = {'summary': summary, 'topic': topic, 'form': form}
    return render(request, 'head_hunters/edit_summary.html', context=context)


@login_required
def show_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    topic = summary.topic
    phone = Profile.objects\
                .get(user_id=summary.owner.id).phone_number

    context = {'summary': summary, 'topic': topic, 'phone': phone}
    return render(request, 'head_hunters/show_summary.html', context=context)


@login_required
def delete_summary(request, summary_id):
    summary = Summary.objects.get(id=summary_id)
    topic = summary.topic
    Summary.objects.filter(id=summary_id).delete()

    context = {'topic': topic}
    return render(request, 'head_hunters/delete_summary.html', context=context)


@login_required
def new_vacancy(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    if request.method != 'POST':
        form = VacancyForm()
    else:
        form = VacancyForm(data=request.POST)
        if form.is_valid():
            new_vacancy = form.save(commit=False)
            new_vacancy.topic = topic
            new_vacancy.owner = request.user
            new_vacancy.company_name = Profile.objects\
                .get(user_id=request.user.id).company_name
            new_vacancy.save()
            return redirect('head_hunters:topic', topic_slug=topic_slug)

    context = {'topic': topic, 'form': form}
    return render(request, 'head_hunters/new_vacancy.html', context=context)


@login_required
def edit_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    topic = vacancy.topic

    check_object_owner(vacancy, request)

    if request.method != 'POST':
        form = VacancyForm(instance=vacancy)
    else:
        form = VacancyForm(instance=vacancy, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('head_hunters:topic', topic_slug=topic.slug)

    context = {'vacancy': vacancy, 'topic': topic, 'form': form}
    return render(request, 'head_hunters/edit_vacancy.html', context=context)


@login_required
def show_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    topic = vacancy.topic
    phone = Profile.objects\
                .get(user_id=vacancy.owner.id).phone_number

    context = {'vacancy': vacancy, 'topic': topic, 'phone': phone}
    return render(request, 'head_hunters/show_vacancy.html', context=context)


@login_required
def delete_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    topic = vacancy.topic
    Vacancy.objects.filter(id=vacancy_id).delete()

    context = {'topic': topic}
    return render(request, 'head_hunters/delete_vacancy.html', context=context)
