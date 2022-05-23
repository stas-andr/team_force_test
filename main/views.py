from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from .forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html')


class CandidateLoginView(LoginView):
    template_name = 'main/login.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')