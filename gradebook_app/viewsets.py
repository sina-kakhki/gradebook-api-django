from rest_framework import viewsets, permissions
from .models import Course, Semester, Lecturer, Student, Class, StudentEnrollment
from .serializers import *


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsLecturerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_lecturer


class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_student


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsAdminUser]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsAdminUser]


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsAdminUser]


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsAdminUser]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsAdminUser]


class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    # Apply permissions for administrator functions
    permission_classes = [IsLecturerUser, IsStudentUser, IsAdminUser]


class MarkViewSet(viewsets.ModelViewSet):
    queryset = StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer

    def get_permissions(self):
        user = self.request.user

        if user.groups.filter(name='Lecturer').exists():
            # Apply permissions for lecturers
            permission_classes = [IsLecturerUser]
        elif user.groups.filter(name='Student').exists():
            # Apply permissions for students
            permission_classes = [IsStudentUser]
        else:
            # Apply default permissions for other user roles (e.g., administrators)
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

