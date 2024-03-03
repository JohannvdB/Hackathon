from django.contrib import admin
from .models import Convener, Specialisations, Student, Module, Academic, StudentAcademic, StudentModuleMark, ModuleAcademic, AcademicSpecialisations, StudentPreferredSpecialisations


# Register your models here.
admin.site.register(Convener)
admin.site.register(Specialisations)
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Academic)
admin.site.register(StudentAcademic)
admin.site.register(StudentModuleMark)
admin.site.register(ModuleAcademic)
admin.site.register(AcademicSpecialisations)
admin.site.register(StudentPreferredSpecialisations)