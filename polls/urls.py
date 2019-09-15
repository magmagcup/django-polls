from django.urls import path

from . import views

app_name = 'polls'
# urlpatterns = [
#     # /polls/
#     # path('polls/brahbrah.html', views.index, name='index'),
#     # Don't need to add .html
#
#     path('', views.index, name='index'),
#     # /polls/1/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # /polls/1/results/
#     path('<int:question_id>/results/', views.result, name='results'),
#     # /polls/1/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
