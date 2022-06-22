from django.db import models


# Create your models here.
class Location(models.Model):
    """
    место для работы специалиста.
    В одном месте в одно время может работать только один специалист
    """
    name = models.CharField(max_length=128)
    cabinet = models.IntegerField()

    def __str__(self):
        return f'{self.name}, cabinet: {self.cabinet}'


class Worker(models.Model):
    """
    специалист, предоставляющий услугу
    """
    name = models.CharField(max_length=128)
    specialities = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """
    временной отрезок работы специалиста.
    Для каждого рабочего дня можно устанавливать отдельный отрезок,
    также в один день можно установить несколько рабочих отрезков
    (например, с 8:00 до 10:00 и с 17:00 до 21:00 того же дня)
    """
    specialist = models.ForeignKey(Worker, on_delete=models.CASCADE,
                                   related_name='specialist',
                                   null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 related_name='location',
                                 null=True)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ['specialist', 'location', 'date', 'start_time',
                           'end_time']

    def __str__(self):
        return f'{self.specialist.name}, schedule: {self.date}, {self.start_time}-{self.end_time}'


class Appointment(models.Model):
    """
    забронированная запись на прием, создаваемая администратором.
    Запись должна содержать время начала и время конца
    (разные процедуры могут занимать разное время)
    """
    client = models.CharField(max_length=128)
    procedure = models.CharField(max_length=128)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE,
                                 related_name='appointments')
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return f'{self.client}, ' \
               f'schedule: {self.schedule.specialist}, ' \
               f'procedure: {self.procedure}'
