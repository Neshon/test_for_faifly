from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register('staff/locations', views.LocationViewSet)
router.register('staff/workers', views.WorkerViewSet)
router.register('staff/schedule', views.ScheduleViewSet)
router.register('staff/appointment', views.AppointmentViewSet)

router.register('client/schedule', views.TimetableViewSet)


urlpatterns = [
    path('v1/docs/', include_docs_urls(title='Service API')),
    path('v1/', include(router.urls))
]
