# Generated by Django 3.2 on 2021-05-27 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210527_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Задача')),
                ('date', models.DateField(verbose_name='Срок задачи')),
                ('date_done', models.DateField(auto_now=True, verbose_name='Дата выполнения')),
                ('executor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.personal')),
            ],
        ),
    ]
