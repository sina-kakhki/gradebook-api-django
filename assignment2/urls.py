from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'semesters', viewsets.SemesterViewSet)
router.register(r'courses', viewsets.CourseViewSet)

urlpatterns = [
    # Other URL patterns
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
]
