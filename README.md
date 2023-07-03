# gradebook-api-django

This is the back-end of the django based gradebook app. Being handled with django's REST framework using APIs.

This implementation includes:

# Models and Serializers									
1.	Course
2.	Semester
3.	Lecturer
4.	Student
5.	Class
6.	StudentEnrollment

# ViewSets and permissions:                                                                 

1.	View for administrator to create/update/delete/show semesters 
2.	View for administrator to create/update/delete/show courses
3.	View for administrator to create/update/delete/show classes
4.	View for administrator to create/update/delete/show lecturers 
5.	View for administrator to assign/remove/change/show a lecturer to a class
6.	View for administrator to create/update/delete/show a student
7.	View for administrator to enrol/remove/show student to classes
8.	View for administrator to upload students from excel files to the website  
9.	View for the gradebook system to email students when their marks are released
10.	View for lecturer to login to the gradebook
11.	View for lectures to enter students’ marks in the gradebook
12.	View for student’s to login to the gradebook
13.	View for students to view their marks in the gradebook 
