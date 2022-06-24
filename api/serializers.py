from rest_framework import serializers

from service.models import Location, Worker, Schedule, Appointment


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

    def validate(self, data):
        schedule = Schedule.objects.filter(location=data['location'],
                                           date=data['date'])
        for timeslot in schedule:
            if data['start_time'] < timeslot.end_time:
                if timeslot:
                    raise serializers.ValidationError(
                        "This place is occupied")
                raise serializers.ValidationError(
                    "At this time there is already a schedule")

        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError(
                "Start time cannot go after end time")
        return data


class TimetableSerializer(serializers.ModelSerializer):
    specialist = serializers.CharField(source='specialist.name',
                                       read_only=True)
    specialities = serializers.CharField(source='specialist.specialities',
                                         read_only=True)
    place = serializers.CharField(source='location.name', read_only=True)
    cabinet = serializers.CharField(source='location.cabinet', read_only=True)

    class Meta:
        model = Schedule
        fields = ('specialist', 'specialities', 'place', 'cabinet', 'date',
                  'start_time', 'end_time')


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        schedule = data['schedule']
        if data['end_time'] >= schedule.end_time:
            raise serializers.ValidationError(
                "Working time is over")
        elif schedule.start_time >= data['start_time']:
            raise serializers.ValidationError(
                "Working time has not started yet")

        appointments = Appointment.objects.filter(schedule=data['schedule'])
        for appointment in appointments:
            if data['start_time'] < appointment.end_time:
                raise serializers.ValidationError(
                    "Appointment time is busy")

        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError(
                "Start time cannot go after end time")
        return data
