from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUser(AbstractUser):
    middle_name = models.CharField("Отчество", max_length=150, blank=True)

    def __str__(self):
        return f'{self.username}: {self.last_name} {self.first_name} {self.middle_name}'


class Tag(models.Model):
    class Meta:
        unique_together = (('tag', 'value'),)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
    tag = models.CharField(max_length=40, verbose_name='Категория навыка')
    value = models.CharField(max_length=40, verbose_name='Навык')

    def __str__(self):
        return f'{self.tag}: {self.value}'


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Кандидат')
    hobbies = models.ManyToManyField(Tag, verbose_name='Навыки')
    def __str__(self):
        return f'{self.user.__str__()}'


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=instance)







