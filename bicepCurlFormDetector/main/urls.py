from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    path( "", views.IndexView.as_view(), name='index' ),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /poplls/5/vote/
    path("<int:pk>/vote/", views.vote, name="vote"),
]