from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, NotFound
from django.views.generic import View
from .models import Convener, Specialisations, Student, Module, Academic, StudentAcademic, StudentModuleMark, ModuleAcademic, AcademicSpecialisations, StudentPreferredSpecialisations
from .serializers import AcademicAndSpecialisationSerializer, AddStudentPreferredSpecialisationsSerializer, SpecialisationSerializer, StudentPreferredSpecialisationsSerializer, StudentModuleMarkSerializer, StudentPreferredSpecialisationsSerializer

# Create your views here.
class StudentModuleMarkListView(View):
    def get(self, request, student_id, *args, **kwargs):
        # retrieve marks
        student_marks = StudentModuleMark.objects.filter(urn_id=student_id)
        serializer = StudentModuleMarkSerializer(student_marks, many=True)
        return JsonResponse(serializer.data, safe=False)

class SpecialisationsListView(View):
    def get(self, request):
        specialisations = Specialisations.objects.all()
        serializer = SpecialisationSerializer(specialisations, many=True)
        return JsonResponse(serializer.data, safe=False)
    

class AddStudentPreferredSpecialisations(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        specialisation_id = request.data.get('specialisation')

        if not (student_id and specialisation_id):
            return Response({'error': 'Both a student and specialisation are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student = Student.objects.get(pk=student_id)
            specialisation = Specialisations.objects.get(pk=specialisation_id)
        except Student.DoesNotExist:
            return Response({'error': f'Student with ID {student_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Specialisations.DoesNotExist:
            return Response({'error': f'Specialisation with ID {specialisation_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        preference = StudentPreferredSpecialisations(student=student, specialisation=specialisation)
        preference.save()

        serializer = StudentPreferredSpecialisationsSerializer(preference)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class StudentAndStudentPreferencesList(APIView):
    def get(self, request):
        # Retrieve all students with their preferred specialisations
        students_with_specialisations = Student.objects.prefetch_related('studentpreferredspecialisations_set')
        serializer = AddStudentPreferredSpecialisationsSerializer(students_with_specialisations, many=True)
        return Response(serializer.data)
    
class AcademicAndSpecialisations(APIView):
    def get(self, request):
        academics_with_specialisations = Academic.objects.prefetch_related('academicspecialisations_set')
        serializer = AcademicAndSpecialisationSerializer(academics_with_specialisations, many=True)
        return Response(serializer.data)
    

class AssignAcademics(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        module_code = request.data.get('module_code')
        moderator_id = request.data.get('moderator_id')
        academic_ids = request.data.get('academic_ids')

        if not (request.data):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            raise NotFound('Student not found')

        try:
            for academic_id in academic_ids:
                is_moderator = (academic_id == moderator_id)
                academic = Academic.objects.get(pk=academic_id)
                student_academic = StudentAcademic.objects.create(
                    urn=student,
                    academic=academic,
                    isModerator=is_moderator
                )

            return Response({'message': 'Academics assigned successfully'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            error_msg = str(e)
            raise APIException(detail=error_msg, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AssignMarks(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        mark_value = request.data.get('mark')
        module_code = request.data.get('module')

        if(not student_id and mark and module):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student = Student.objects.get(urn=student_id)
            module = Module.objects.get(code=module_code)

            student_module_mark, created = StudentModuleMark.objects.get_or_create(
                urn=student,
                moduleCode=module
            )

            if not created:
                student_module_mark.mark = mark_value
                student_module_mark.save()

                return Response({'message': 'Mark updated successfully'}, status=status.HTTP_200_OK)

            else:
                StudentModuleMark.objects.create(
                    urn=student,
                    moduleCode=module,
                    mark=mark_value
                )

                return Response({'message': 'Mark assigned successfully'}, status=status.HTTP_201_CREATED)
        
        except Student.DoesNotExist:
            return Response({'error': f'Student with ID {student_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Module.DoesNotExist:
            return Response({'error': f'Module with code {module_code} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentsByAcademic(APIView):
    def get(self, request, academic_id):
        try:
            # Retrieve the academic instance
            academic = Academic.objects.get(id=academic_id)
            
            # Get all student-academic relationships for the academic
            student_academics = StudentAcademic.objects.filter(academic=academic)
            
            # Extract student IDs
            student_ids = [student_academic.urn_id for student_academic in student_academics]
            
            # Retrieve student instances
            students = Student.objects.filter(urn__in=student_ids)
            
            # Serialize student data
            serialized_students = [{'urn': student.urn, 'name': student.name} for student in students]
            
            return Response({'students': serialized_students}, status=status.HTTP_200_OK)
        
        except Academic.DoesNotExist:
            return Response({'error': f'Academic with ID {academic_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)