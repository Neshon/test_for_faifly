from rest_framework import serializers

from service.models import Location, Worker, Schedule, Appointment


# API для управляющих, позволяющее создавать специалистов, места и рабочее время для них
class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleForClientSerializer(serializers.ModelSerializer):
    specialist = serializers.CharField(source='specialist.name', read_only=True)
    specialities = serializers.CharField(source='specialist.specialities', read_only=True)
    place = serializers.CharField(source='location.name', read_only=True)
    cabinet = serializers.CharField(source='location.cabinet', read_only=True)

    class Meta:
        model = Schedule
        fields = ('specialist', 'specialities', 'place', 'cabinet', 'date', 'start_time', 'end_time')


class AppointmentSerializer(serializers.ModelSerializer):
    # schedule = ScheduleSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
