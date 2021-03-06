# Generated by Django 3.2 on 2021-05-27 01:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_installation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 27, 1, 34, 59, 990077, tzinfo=utc), verbose_name='Завершение проекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date_filming',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 27, 1, 35, 5, 811988, tzinfo=utc), verbose_name='Дата съемки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='installation',
            field=models.CharField(blank=True, max_length=150, verbose_name='Монтажник'),
        ),
        migrations.AddField(
            model_name='event',
            name='material_link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на иатериалы'),
        ),
        migrations.AddField(
            model_name='event',
            name='pay_status',
            field=models.CharField(choices=[('no', 'Не оплачено'), ('fifty', 'Предоплата'), ('yes', 'Оплачено')], default='no', max_length=5, verbose_name='Статус оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='rent',
            field=models.CharField(default='asdf', max_length=100, verbose_name='Аренда оборудования'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дедлайн'),
        ),
    ]
