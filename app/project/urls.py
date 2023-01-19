from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from employees.views import PositionListCreateAPIView, PositionRetrieveUpdateDestroyAPIView, EmployeeViewSet
from accounts.views import ProfileRegisterAPIView
router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('register', ProfileRegisterAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/positions/', PositionListCreateAPIView.as_view()),
    path('api/positions/<int:id>/', PositionRetrieveUpdateDestroyAPIView.as_view()),
    path('api/', include(router.urls)),

]
