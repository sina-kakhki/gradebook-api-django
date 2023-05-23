import openpyxl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView

from gradebook.forms import SemesterForm, CourseForm, ClassForm, LecturerForm, StudentForm, StudentEnrollmentForm, \
    DeleteSemesterForm, AssignClassForm, UploadStudentsForm
from gradebook.models import *


# Administrator views
@login_required
def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'semester_list.html', {'semesters': semesters})


@login_required
def semester_create(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'semester_form.html', {'form': form})


@login_required
def semester_detail(request, pk):
    semester = Semester.objects.get(pk=pk)
    return render(request, 'semester_detail.html', {'semester': semester})


@login_required
def semester_update(request, pk):
    semester = Semester.objects.get(pk=pk)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm(instance=semester)
    return render(request, 'semester_form.html', {'form': form})


@login_required
def semester_delete(request, pk):
    semester = Semester.objects.get(pk=pk)
    semester.delete()
    return redirect('semester_list')


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


@login_required
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})


@login_required
def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})


@login_required
def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('course_list')


@login_required
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})


@login_required
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'class_form.html', {'form': form})


@login_required
def class_detail(request, pk):
    class_obj = Class.objects.get(pk=pk)
    return render(request, 'class_detail.html', {'class': class_obj})


@login_required
def class_update(request, pk):
    class_obj = Class.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=class_obj)
    return render(request, 'class_form.html', {'form': form})


@login_required
def class_delete(request, pk):
    class_obj = Class.objects.get(pk=pk)
    class_obj.delete()
    return redirect('class_list')


@login_required
def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturer_list.html', {'lecturers': lecturers})


@login_required
def lecturer_create(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm()
    return render(request, 'lecturer_form.html', {'form': form})


@login_required
def lecturer_detail(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    return render(request, 'lecturer_detail.html', {'lecturer': lecturer})


@login_required
def lecturer_update(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'lecturer_form.html', {'form': form})


@login_required
def lecturer_delete(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    lecturer.delete()
    return redirect('lecturer_list')


@login_required
def assign_lecturer(request, class_pk):
    class_obj = Class.objects.get(pk=class_pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            lecturer = form.cleaned_data['lecturer']
            class_obj.lecturer = lecturer
            class_obj.save()
            return redirect('class_list')
    else:
        form = LecturerForm()
    return render(request, 'assign_lecturer.html', {'form': form, 'class': class_obj})


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})


@login_required
def student_grades(request):
    student_id = request.GET.get('id')

    enrollment = get_object_or_404(StudentEnrollment, studentID__id=student_id)
    grades = enrollment.grade

    return render(request, 'student_grade.html', {'enrollment': enrollment, 'grades': grades})


@login_required
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')


@login_required
def enroll_student(request, class_pk):
    class_obj = Class.objects.get(pk=class_pk)
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            grade = form.cleaned_data['grade']
            enrol_time = form.cleaned_data['enrol_time']
            grade_time = form.cleaned_data['grade_time']
            enrollment = StudentEnrollment(student=student, class_obj=class_obj, grade=grade,
                                           enrol_time=enrol_time, grade_time=grade_time)
            enrollment.save()
            return redirect('class_detail', pk=class_pk)
    else:
        form = StudentEnrollmentForm()
    return render(request, 'enroll_student.html', {'form': form, 'class': class_obj})


@login_required
def remove_student(request, enrollment_pk):
    enrollment = StudentEnrollment.objects.get(pk=enrollment_pk)
    class_pk = enrollment.class_obj.pk
    enrollment.delete()
    return redirect('class_detail', pk=class_pk)


@login_required
def student_enrollment_list(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    enrollments = student.studentenrollment_set.all()
    return render(request, 'student_enrollment_list.html', {'student': student, 'enrollments': enrollments})


# Login and Logout views
# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active:
#             # User will be redirected to homepage with different views
#             login(request, user)
#             return redirect('index')
#         else:
#             # Invalid credentials or user is inactive
#             error_message = 'Invalid login credentials'
#             return render(request, 'registration/login.html', {'error_message': error_message})


def login_user(request):
    error_message = None  # Set default error message to None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid login credentials'
    return render(request, 'registration/login.html', {'error_message': error_message})



def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def assign_class(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        form = AssignClassForm(request.POST)
        if form.is_valid():
            class_id = form.cleaned_data['class']
            class_obj = get_object_or_404(Class, id=class_id)
            lecturer.class_assigned = class_obj
            lecturer.save()
            return redirect('view_lecturer', pk=lecturer_id)
    else:
        form = AssignClassForm()

    context = {'form': form, 'lecturer': lecturer}
    return render(request, 'assign_class.html', context)


class HomeView(TemplateView):
    template_name = 'index.html'


def create_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()

    context = {'form': form}
    return render(request, 'create_semester.html', context)


def view_semester(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    context = {'semester': semester}
    return render(request, 'view_semester.html', context)


def update_semester(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('view_semester', semester_id=semester_id)
    else:
        form = SemesterForm(instance=semester)

    context = {'form': form, 'semester': semester}
    return render(request, 'update_semester.html', context)


def delete_semester(request, semester_id):
    semester = Semester.objects.get(id=semester_id)

    if request.method == 'POST':
        form = DeleteSemesterForm(request.POST, instance=semester)
        if form.is_valid():
            semester.delete()
            return redirect('semester_list')
    else:
        form = DeleteSemesterForm(instance=semester)

    context = {
        'semester': semester,
        'form': form,
    }
    return render(request, 'delete_semester.html', context)


def view_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})


def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})


def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'create_class.html', {'form': form})


def view_class(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    return render(request, 'view_class.html', {'class_obj': class_obj})


def update_class(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)

    if request.method == 'POST':
        form = ClassForm(request.POST, instance=_class)
        if form.is_valid():
            form.save()
            return redirect('view_class', class_id=class_id)
    else:
        form = ClassForm(instance=_class)

    context = {
        'form': form,
        'class_id': class_id
    }
    return render(request, 'update_class.html', context)


def delete_class(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)

    if request.method == 'POST':
        _class.delete()
        messages.success(request, 'Class deleted successfully.')
        return redirect('index')

    context = {
        'class': _class
    }
    return render(request, 'delete_class.html', context)


def create_lecturer(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            lecturer = form.save()
            return redirect('lecturer_detail', pk=lecturer.pk)
    else:
        form = LecturerForm()
    return render(request, 'lecturer_form.html', {'form': form})


def view_lecturer(request, lecturer_id):
    # Retrieve the lecturer object from the database
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)

    context = {
        'lecturer': lecturer
    }

    return render(request, 'lecturer_detail.html', context)


def update_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_detail', lecturer_id=lecturer_id)
    else:
        form = LecturerForm(instance=lecturer)

    return render(request, 'lecturer_form.html', {'form': form})


def delete_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, pk=lecturer_id)

    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturer_list')

    return render(request, 'delete_lecturer.html', {'lecturer': lecturer})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})


def update_student(request, student_id):
    student = Student.get_student(student_id)
    if not student:
        return HttpResponseNotFound("Student not found.")

    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('view_student', student_id=student_id)

    return render(request, 'student_form.html', {'form': form, 'edit_mode': True})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})


def view_student_enrollment(request, pk):
    enrollment = StudentEnrollment.objects.get(pk=pk)
    return render(request, 'view_student_enrollment.html', {'enrollment': enrollment})


def update_student_enrollment(request, pk):
    enrollment = get_object_or_404(StudentEnrollment, pk=pk)
    form = StudentEnrollmentForm(instance=enrollment)

    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('view_student_enrollment', pk=pk)

    return render(request, 'update_student_enrollment.html', {'form': form, 'enrollment': enrollment})


def delete_student_enrollment(request, pk):
    enrollment = get_object_or_404(StudentEnrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('student_enrollment_list')

    return render(request, 'delete_student_enrollment.html', {'enrollment': enrollment})


def upload_students(request):
    if request.method == 'POST':
        form = UploadStudentsForm(request.POST, request.FILES)
        if form.is_valid():
            # Get uploaded file
            file = form.cleaned_data['file']

            # Process the file data
            students = process_uploaded_file(file)

            # Create student records
            for student_data in students:
                student = Student.objects.create(**student_data)

            # Redirect to student list
            return redirect('student_list')
    else:
        form = UploadStudentsForm()

    return render(request, 'upload_students.html', {'form': form})


def process_uploaded_file(file):
    # Process the uploaded file data (Excel format)
    # Extract and validate student data from the file
    # Return a list of dictionaries, each containing student data

    students = []
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook.active

    for row in worksheet.iter_rows(min_row=2, values_only=True):
        student_data = {
            'student_id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'email': row[3],
            'date_of_birth': row[4],
        }
        students.append(student_data)

    return students


@login_required
def send_marks_email(request):
    # Logic to retrieve the necessary information for sending the email
    # such as the student, marks, email template, etc.

    # Compose the email content
    subject = 'Your Marks/Grades'
    message = 'Your marks are available, please login to the gradebook to view them '
    from_email = 'sender@example.com'
    recipient_email = 'recipient@example.com'

    # Send the email
    send_mail(subject, message, from_email, [recipient_email])

    # Redirect to a success page or another appropriate URL
    return redirect('home')
