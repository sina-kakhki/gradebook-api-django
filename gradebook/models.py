import datetime

from django.db import models


class Semester(models.Model):
    semesterID = models.CharField(max_length=4, default=1)
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=50)


class Course(models.Model):
    courseID = models.CharField(max_length=6, default=1)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')


class Lecturer(models.Model):
    staffID = models.CharField(max_length=7)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    DOB = models.DateField()
    course = models.ManyToManyField(Course)


class Student(models.Model):
    studentID = models.CharField(max_length=6)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    DOB = models.DateField()


class Class(models.Model):
    classID = models.CharField(max_length=8, default=1)
    number = models.CharField(max_length=50)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)


class StudentEnrollment(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='classID', default=1)
    enrollment_date = models.DateField(default=datetime.date.today)
    grade_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=50)
