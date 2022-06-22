from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from . import serializers

from .permissions import IsAdministrator, IsManager

from service.models import Location, Worker, Schedule, Appointment


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (IsManager,)

    # def perform_create(self, serializer):
    #     serializer.save(username=self.request.user)
    #
    # def get_queryset(self):
    #     return super().get_queryset().filter(username=self.request.user)


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    permission_classes = (IsManager,)

    # def perform_create(self, serializer):
    #     serializer.save(username=self.request.user)
    #
    # def get_queryset(self):
    #     return super().get_queryset().filter(username=self.request.user)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    permission_classes = (IsManager,)

    # def perform_create(self, serializer):
    #     serializer.save(username=self.request.user)
    #
    # def get_queryset(self):
    #     return super().get_queryset().filter(username=self.request.user)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = (IsAdministrator,)

    def perform_create(self, serializer):
        print(self)
        print(serializer)
        serializer.save()


class ScheduleForClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = serializers.ScheduleForClientSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'specialist__specialities']
