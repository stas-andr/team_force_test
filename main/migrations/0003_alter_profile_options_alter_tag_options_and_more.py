# Generated by Django 4.0.4 on 2022-05-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_myuser_middle_name_tag_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=40, unique=True, verbose_name='Категория навыка'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.CharField(max_length=40, verbose_name='Навык'),
        ),
    ]
