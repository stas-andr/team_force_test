from django.urls import path

from .views import index
from .views import CandidateLoginView
from .views import CandidateLogoutView
from .views import profile
from .views import RegisterUserView, RegisterDoneView

app_name = 'main'
urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', CandidateLoginView.as_view(), name='login'),
    path('accounts/logout/', CandidateLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('', index, name='index'),
]