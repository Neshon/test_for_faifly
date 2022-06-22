from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()

router.register('personal/locations', views.LocationViewSet)
router.register('personal/workers', views.WorkerViewSet)
router.register('personal/schedule', views.ScheduleViewSet)
router.register('personal/appointment', views.AppointmentViewSet)

router.register('client/schedule', views.ScheduleForClientViewSet)


urlpatterns = [
    path('v1/docs/', include_docs_urls(title='Service API', public=False)),

    path('v1/', include(router.urls))
]
