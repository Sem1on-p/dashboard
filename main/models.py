from django.db import models
import smtplib
import datetime


# Create your models here.
class Personal(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    rang = models.CharField('Должность', max_length=50)

    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

class Event(models.Model):
    event_status_choise = [
        ('potential', 'Потенциальный'),
        ('job', 'В работе'),
        ('completed', 'Завершен')
    ]
    event_type_choise = [
        ('installation', 'Монтаж'),
        ('report roller', 'Отчетный видеоролик'),
        ('interior photography', 'Интерьерная съемка'),
        ('survey', 'Съемка'),
        ('on-line translation', 'Онлайн трансляция'),
        ('filming and online broadcasting', 'Съемка и онлайн трансляция')
    ]

    installation_status_choise = [
        ('y', 'Есть'),
        ('n', 'Нет')
    ]

    pay_status_choise = [
        ('no', 'Не оплачено'),
        ('fifty', 'Предоплата'),
        ('yes', 'Оплачено')
    ]

    event = models.CharField('Event', max_length=100)
    description = models.TextField('Описание')
    event_status = models.CharField('Статус мероприятия', max_length=20, choices=event_status_choise)
    event_type = models.CharField('Тип мероприятия', max_length=40, choices=event_type_choise)
    email = models.CharField('e-Mail заказчика', max_length=100)
    date = models.DateField('Дедлайн', blank=True)
    personal = models.ManyToManyField(Personal)
    installation_status = models.CharField('Монтаж статус', max_length=1, choices=installation_status_choise)
    installation = models.CharField('Монтажник', max_length=150, blank=True)
    date_filming = models.DateField('Дата съемки', blank=True)
    material_link = models.CharField('Ссылка на иатериалы', max_length=200, blank=True)
    pay_status = models.CharField('Статус оплаты', max_length=5, choices=pay_status_choise)
    rent = models.CharField('Аренда оборудования', max_length=100)
    date_end = models.DateField('Завершение проекта', blank=True)
    budget = models.IntegerField('Бюджет', blank=True, default=0)
    costs = models.IntegerField('Расходы', blank=True, default=0)
    remnant = models.IntegerField('Остаток', blank=True, default=0)

    def __str__(self):
        return f'{str(self.id)} {self.event}'

    def personal_list(self):
        x = Personal.objects.filter(event=self)
        return x

    def save(self, *args, **kwargs):
        self.remnant = self.budget - self.costs
        return super().save(*args, **kwargs)

    def deadline_status(self):
        if (self.date - datetime.datetime.now().date()).days <= 5:
            return True
        else:
            return False

    def __send_message(self):
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.ehlo()
        server.login('scope-it@yandex.ru', 'itprogress228')
        message = 'Jopa'
        server.sendmail('scope-it@yandex.ru', self.email, message)
        server.quit()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        
class Task(models.Model):
    text = models.CharField('Задача', max_length=200)
    executor = models.ForeignKey(Personal, blank=True, on_delete=models.CASCADE)
    date = models.DateField('Срок задачи')

class Task_archive(models.Model):
    text = models.CharField('Задача', max_length=200)
    executor = models.ForeignKey(Personal, blank=True, on_delete=models.CASCADE)
    date = models.DateField('Срок задачи')
    date_done = models.DateField('Дата выполнения', auto_now=True)
