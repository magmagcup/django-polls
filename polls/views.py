from django.http import Http404, HttpResponseRedirect
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import Question, Choice, Vote


def index(request):
    # redirect user to the polls index
    return HttpResponseRedirect(reverse('polls:index'))
    # newest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in newest_question_list])
    # return HttpResponse(output)

    # template = loader.get_template('polls/index.html')
    # context = {
    #     'newest_question_list': newest_question_list,
    # }
    #
    # return HttpResponse(template.render(context, request))
    # newest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'newest_question_list': newest_question_list}
    # return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse(f"You're looking at question {question_id}.")
    question = get_object_or_404(Question, pk=question_id)
    user_vote = Vote.objects.filter(user=request.user,vote_question=question)
    return render(request, 'polls/detail.html', {'question': question, 'u_vote': user_vote})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        messages.error(request, f"You didn't make a choice")
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if already_vote(request.user, question):
            user_vote = Vote.objects.filter(user=request.user, vote_question=question)[0]
            user_vote.change_vote(selected_choice)

        else:
            new_v = Vote(vote_question=question, choice=selected_choice, user=request.user)
            new_v.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    messages.success(request, "Your choice successfully recorded. Thank you.")
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def same_question(request_user,question_user,choice_user):
    user_vote = Vote.objects.filter(user=request_user, vote_question=question_user)
    if user_vote:
        return True
    return False


def already_vote(request_user,question_user):
    user_vote = Vote.objects.filter(user=request_user, vote_question=question_user)
    if user_vote.count():
        return True
    else:
        return False


def signup(request):
    """Register a new user."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username,raw_password = raw_password)
            login(request, user)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'newest_question_list'

    def get_queryset(self):
        """Return the recently published questions.(not include question in the future)"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


def page404(request, exception):
    return render(request, 'polls/404.html')
