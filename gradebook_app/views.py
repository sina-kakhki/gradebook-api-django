from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from gradebook_app.models import *
import pandas as pd
from django.db import transaction


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
