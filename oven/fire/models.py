from django.db import models

# Create your models here.
class Convener(models.Model):
    name = models.CharField(max_length=50)

class Specialisations(models.Model):
    specialisation = models.CharField(max_length=100, primary_key=True)

class Student(models.Model):
    urn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Module(models.Model):
    code = models.CharField(max_length=7, primary_key=True)
    module_convener = models.ForeignKey(Convener, on_delete=models.CASCADE)

class Academic(models.Model):
    name = models.CharField(max_length=50)

class StudentAcademic(models.Model):
    isModerator = models.BooleanField(default=False)
    urn = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE)

class StudentModuleMark(models.Model):
    urn = models.ForeignKey(Student, on_delete=models.CASCADE)
    moduleCode = models.ForeignKey(Module, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True)

class ModuleAcademic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE)

class AcademicSpecialisations(models.Model):
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE)
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE)

class StudentPreferredSpecialisations(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE)