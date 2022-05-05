# Generated by Django 4.0.4 on 2022-05-05 06:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('internal_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id', models.PositiveIntegerField(unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='наименование')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='создана')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='обновлена')),
                ('clues_count', models.PositiveIntegerField(verbose_name='количество ключей')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('internal_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id', models.PositiveIntegerField(unique=True, verbose_name='ID')),
                ('answer', models.CharField(max_length=128, verbose_name='ответ')),
                ('question', models.TextField(verbose_name='вопрос')),
                ('value', models.PositiveIntegerField(null=True, verbose_name='стоимость')),
                ('airdate', models.DateTimeField(null=True, verbose_name='дата эфира')),
                ('created_at', models.DateTimeField(null=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='дата обновления')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
    ]