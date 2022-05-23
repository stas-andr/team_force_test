from django.urls import path

from .views import index
from .views import CandidateLoginView
from .views import RegisterUserView

app_name = 'main'
urlpatterns = [
    path('accounts/login/', CandidateLoginView.as_view(), name='login'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('', index, name='index'),
]