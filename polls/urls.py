from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    # path('polls/brahbrah.html', views.index, name='index'),
    # Don't need to add .html

    path('', views.index, name='index'),
    # /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/1/results/
    path('<int:question_id>/results/', views.result, name='results'),
    # /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
