from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view()),
    # path('<int:pk>/', profile_view.DetailView.as_view()),
]
