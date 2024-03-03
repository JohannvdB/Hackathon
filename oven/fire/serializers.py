from rest_framework import serializers
from .models import Convener, Specialisations, Student, Module, Academic, StudentAcademic, StudentModuleMark, ModuleAcademic, AcademicSpecialisations, StudentPreferredSpecialisations

def serialize_student_marks(student_marks):
    data = []
    for mark in student_marks:
        data.append({ 'module_code': mark.moduleCode.code, 'mark': mark.mark.mark })
    return data

class StudentModuleMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModuleMark
        fields = ['moduleCode', 'mark']

class SpecialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialisations
        fields = ['specialisation']

class StudentPreferredSpecialisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPreferredSpecialisations
        fields = '__all__' # cool syntax use this

class AddStudentPreferredSpecialisationsSerializer(serializers.ModelSerializer):
    preferred_specialisation = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['urn', 'name', 'preferred_specialisation']

    def get_preferred_specialisation(self, obj):
        try:
            preferred_spec = obj.studentpreferredspecialisations_set.first()
            if preferred_spec:
                return SpecialisationSerializer(preferred_spec.specialisation).data
        except StudentPreferredSpecialisations.DoesNotExist:
            pass
        return None
    
class AcademicAndSpecialisationSerializer(serializers.ModelSerializer):
    specialisations = serializers.SerializerMethodField()

    class Meta:
        model = Academic
        fields = ['id', 'name', 'specialisations']

    def get_specialisations(self, obj):
        try:
            academic_specialisations = obj.academicspecialisations_set.all()
            if academic_specialisations:
                return [spec.specialisation.specialisation for spec in academic_specialisations]
        except AcademicSpecialisations.DoesNotExist:
            pass
        return []