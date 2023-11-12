from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # The path function has four arguments:
    # route
    # view
    # `kwargs`: Arbitrary keyword arguments can be passed in a dictionary to the target view.
    # `name`: Naming your URL lets you refer to it unambiguously from elsewhere in Django, 
    #         especially from within templates. 
    
    # Function based
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
    # Class based
    # <question_id> is changed to <pk>
    # This is necessary because we’ll use the DetailView generic view to replace 
    # our detail() and results() views, and it expects the primary key value 
    # captured from the URL to be called "pk".
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('your-name/', views.get_name, name='name-form'),
]