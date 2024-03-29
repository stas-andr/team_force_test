import floppyforms
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import MyUser
from .models import Tag

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль еще раз для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
                  'password1', 'password2')


class AddHobbyForm(forms.ModelForm):
    tag = forms.CharField(label='Категория навыка', widget=floppyforms.widgets.Input(datalist=Tag.objects.values_list("tag", flat=True).distinct()))
    value = forms.CharField(label='Навык', widget=floppyforms.widgets.Input(datalist=Tag.objects.values_list("value", flat=True).distinct()))

    class Meta:
        model = Tag
        fields = '__all__'
    
