from rest_framework import serializers
from .models import Semester, Course, Lecturer, Student, Class, StudentEnrollment


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'semesterID', 'year', 'semester')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'courseID', 'code', 'name', 'semester')


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'staffID', 'firstName', 'lastName', 'email', 'DOB', 'course')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'studentID', 'firstName', 'lastName', 'email', 'DOB')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'classID', 'number', 'semester', 'course', 'lecturer', 'students')


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = ('id', 'studentID', 'enrolled_class', 'enrollment_date', 'grade_date', 'grade')
