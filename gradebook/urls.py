from django.urls import path
from gradebook import views

urlpatterns = [
    # Index and Home
    path('', views.HomeView.as_view(), name='index'),

    # Semester URLs
    path('semester/', views.semester_list, name='semester_list'),
    path('semester/create/', views.create_semester, name='create_semester'),
    path('semester/<int:pk>/', views.view_semester, name='view_semester'),
    path('semester/<int:pk>/update/', views.update_semester, name='update_semester'),
    path('semester/<int:pk>/delete/', views.delete_semester, name='delete_semester'),

    # Course URLs
    path('course/', views.course_list, name='course_list'),
    path('course/create/', views.create_course, name='create_course'),
    path('course/<int:pk>/', views.view_course, name='view_course'),
    path('course/<int:pk>/update/', views.update_course, name='update_course'),
    path('course/<int:pk>/delete/', views.delete_course, name='delete_course'),

    # Class URLs
    path('class/', views.class_list, name='class_list'),
    path('class/create/', views.create_class, name='create_class'),
    path('class/<int:pk>/', views.view_class, name='view_class'),
    path('class/<int:pk>/update/', views.update_class, name='update_class'),
    path('class/<int:pk>/delete/', views.delete_class, name='delete_class'),

    # Lecturer URLs
    path('lecturer/', views.lecturer_list, name='lecturer_list'),
    path('lecturer/create/', views.create_lecturer, name='create_lecturer'),
    path('lecturer/<int:pk>/', views.view_lecturer, name='view_lecturer'),
    path('lecturer/<int:pk>/update/', views.update_lecturer, name='update_lecturer'),
    path('lecturer/<int:pk>/delete/', views.delete_lecturer, name='delete_lecturer'),
    path('lecturer/<int:lecturer_id>/assign_class/', views.assign_class, name='assign_class'),

    # Student URLs
    path('student/', views.student_list, name='student_list'),
    path('student/create/', views.create_student, name='create_student'),
    path('student/<int:pk>/', views.student_detail, name='view_student'),
    path('student/<int:pk>/update/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('student/<int:pk>/enroll/', views.enroll_student, name='enroll_student'),
    path('student/enrollment/', views.student_enrollment_list, name='student_enrollment_list'),
    path('student/enrollment/<int:pk>/', views.view_student_enrollment, name='view_student_enrollment'),
    path('student/enrollment/<int:pk>/update/', views.update_student_enrollment, name='update_student_enrollment'),
    path('student/enrollment/<int:pk>/delete/', views.delete_student_enrollment, name='delete_student_enrollment'),

    # Other URLs
    path('upload_students/', views.upload_students, name='upload_students'),
    path('send_marks_email/', views.send_marks_email, name='send_marks_email'),
    path('student/grades/', views.student_grades, name='student_grades'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
