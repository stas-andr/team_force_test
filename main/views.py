from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import RegisterUserForm
from .forms import AddHobbyForm
from .models import MyUser, Profile, Tag


def index(request):
    return render(request, 'main/index.html')


class CandidateLoginView(LoginView):
    template_name = 'main/login.html'


class CandidateLogoutView(LogoutView):
    template_name = 'main/logout.html'


@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user.pk)
    hobbies = {}
    for hobby in profile.hobbies.all():
        if hobby.tag not in hobbies.keys():
            hobbies[hobby.tag] = []
        hobbies[hobby.tag].append(hobby.value)
    if request.method == 'POST':
        hobby_form = AddHobbyForm(request.POST)
        if hobby_form.is_valid():
            hobby = hobby_form.save()
            profile.hobbies.add(hobby)
            hobbies[hobby.tag].append(hobby.value)
            messages.add_message(request, messages.SUCCESS, 'Навык добавлен')
            return redirect('main:profile')
        else:
            messages.add_message(request, messages.WARNING, 'Навык не добавлен')
    else:
        hobby_form = AddHobbyForm()
    for tag in hobbies:
        hobbies[tag] = ", ".join(hobbies[tag])
    context = {'hobbies': hobbies, 'form': hobby_form}
    return render(request, 'main/profile.html', context=context)


class RegisterUserView(CreateView):
    model = MyUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'