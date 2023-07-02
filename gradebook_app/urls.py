from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from gradebook_app import views
from gradebook_app.viewsets import *

router = DefaultRouter()
router.register("semester", SemesterViewSet)
router.register("course", CourseViewSet)
router.register("lecturer", LecturerViewSet)
router.register("student", StudentViewSet)
router.register("class", ClassViewSet)
router.register("enrolment", StudentEnrollmentViewSet)
router.register("marks", MarkViewSet)


urlpatterns = [

    path('', include(router.urls)),

    path('auth/lecturer/', LecturerLoginView, name='lecturer_login'),
    path('auth/student/', StudentLoginView, name='student_login'),

    # Administrator URLs
    path('semesters/', viewsets.SemesterViewSet.as_view({'get': 'list', 'post': 'create'}), name='semester-list'),
    path('semesters/<int:pk>/', viewsets.SemesterViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='semester-detail'),
    path('courses/', viewsets.CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('courses/<int:pk>/', viewsets.CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='course-detail'),

    # Lecturer URLs
    path('lecturers/', viewsets.LecturerViewSet.as_view({'get': 'list'}), name='lecturer-list'),
    path('lecturers/<int:pk>/', viewsets.LecturerViewSet.as_view({'get': 'retrieve'}), name='lecturer-detail'),

    # Student URLs
    path('students/', viewsets.StudentViewSet.as_view({'get': 'list'}), name='student-list'),
    path('students/<int:pk>/', viewsets.StudentViewSet.as_view({'get': 'retrieve'}), name='student-detail'),

    # Class URLs
    path('classes/', viewsets.ClassViewSet.as_view({'get': 'list', 'post': 'create'}), name='class-list'),
    path('classes/<int:pk>/', viewsets.ClassViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='class-detail'),

    # Student Enrollment URLs
    path('student-enrollments/', viewsets.StudentEnrollmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-enrollment-list'),
    path('student-enrollments/<int:pk>/', viewsets.StudentEnrollmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='student-enrollment-detail'),

    # URL for uploading students from an Excel file
    path('students/upload/', views.StudentUploadView.as_view(), name='student-upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
