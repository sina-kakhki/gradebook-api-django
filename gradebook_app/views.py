from rest_framework.parsers import MultiPartParser
from gradebook_app.models import *
import pandas as pd
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import LecturerSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LecturerLoginView(ObtainAuthToken):
    serializer_class = LecturerSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        lecturer = token.user.lecturer
        return Response({'token': token.key, 'lecturer_id': lecturer.pk})


class StudentLoginView(ObtainAuthToken):
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        student = token.user.student
        return Response({'token': token.key, 'student_id': student.pk})


class StudentUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file_obj = request.FILES['file']

        # Read the Excel file using pandas
        df = pd.read_excel(file_obj)

        # Extract student data from the DataFrame
        students_data = df.to_dict(orient='records')

        # Process and save student data in the database
        with transaction.atomic():
            for data in students_data:
                student = Student(
                    studentID=data['studentID'],
                    firstName=data['firstName'],
                    lastName=data['lastName'],
                    email=data['email'],
                    DOB=data['DOB']
                )
                student.save()

        return Response({'message': 'File uploaded successfully'})
