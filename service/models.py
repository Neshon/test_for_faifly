from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=128)
    cabinet = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}, cabinet: {self.cabinet}'


class Worker(models.Model):
    name = models.CharField(max_length=128)
    specialities = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    specialist = models.ForeignKey(Worker, on_delete=models.SET_NULL,
                                   related_name='specialist',
                                   null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 related_name='location',
                                 null=True)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    # available = models.BooleanField(default=True)

    class Meta:
        unique_together = ['specialist', 'location', 'date', 'start_time',
                           'end_time']

    def __str__(self):
        return f'{self.specialist.name}, schedule: {self.date}, ' \
               f'{self.start_time}-{self.end_time}'


class Appointment(models.Model):
    client = models.CharField(max_length=128)
    procedure = models.CharField(max_length=128)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                 null=True, related_name='appointments')
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return f'{self.client}, ' \
               f'schedule: {self.schedule.specialist}, ' \
               f'procedure: {self.procedure}'
