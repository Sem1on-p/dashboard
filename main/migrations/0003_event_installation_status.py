# Generated by Django 3.2 on 2021-05-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_event_personal'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='installation_status',
            field=models.CharField(choices=[('y', 'Есть'), ('n', 'Нет')], default='Есть', max_length=1, verbose_name='Монтаж статус'),
            preserve_default=False,
        ),
    ]
