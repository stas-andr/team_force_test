from django.shortcuts import render
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
    form = AddHobbyForm()
    for hobby in profile.hobby.all():
        if hobby.tag not in hobbies.keys():
            hobbies[hobby.tag] = []
        hobbies[hobby.tag].append(hobby.value)

    for tag in hobbies:
        hobbies[tag] = ", ".join(hobbies[tag])
    if request.method == 'POST':
        h_form = AddHobbyForm(request.POST)
        if h_form.is_valid():
            h_form.save()
            tag_from_form = h_form.cleaned_data.get("tag")
            value_from_form = h_form.cleaned_data.get("value")
            hobby = Tag.objects.create(tag=tag_from_form, value=value_from_form)
            Profile.objects.create(Profile=profile, hobby=hobby)
            messages.add_message(request, messages.SUCCESS, 'Навык добавлен')
        else:
            form = h_form
            messages.add_message(request, messages.WARNING, 'Навык не добавлен')
    context = {'hobbies': hobbies, 'form': form}
    return render(request, 'main/profile.html', context=context)


class RegisterUserView(CreateView):
    model = MyUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'