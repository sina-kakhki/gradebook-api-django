from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Semester, Course, Class, Lecturer, Student, StudentEnrollment


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['year', 'semester']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'semester', 'course', 'lecturer']


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['staffID', 'firstName', 'lastName', 'email', 'course', 'DOB']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'firstName', 'lastName', 'email', 'DOB']


class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment
        exclude = ['enrol_time']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class AssignClassForm(forms.Form):
    lecturer = forms.ModelChoiceField(queryset=Lecturer.objects.all(), empty_label=None, label='Select Lecturer')


class DeleteSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = []  # No fields required for deletion confirmation form


@deconstructible
class FileExtensionValidator:
    def __init__(self, allowed_extensions, message=None):
        self.allowed_extensions = allowed_extensions
        self.message = message

    def __call__(self, value):
        ext = value.name.split('.')[-1]
        if ext not in self.allowed_extensions:
            if self.message is None:
                self.message = f"Only {', '.join(self.allowed_extensions)} file types are allowed."
            raise ValidationError(self.message)


class UploadStudentsForm(forms.Form):
    file = forms.FileField(label='Excel File', validators=[FileExtensionValidator(['xlsx'])])

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Perform any additional validation for the uploaded file if needed
            pass

        return file
