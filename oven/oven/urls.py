"""
URL configuration for oven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fire.api.urls')),
    path('student_marks/<int:student_id>/', views.StudentModuleMarkListView.as_view(), name='student_marks'),
    path('specialisations/', views.AddStudentPreferredSpecialisations.as_view(), name='specialisations_list'),
    path('students', views.StudentAndStudentPreferencesList.as_view(), name="student_preference_list"),
    path('academics', views.AcademicAndSpecialisations.as_view(), name="academic_and_specialisation_list"),
    path('assign_academics', views.AssignAcademics.as_view(), name="assign_academics_to_students"),
    path('assign_mark', views.AssignMarks.as_view(), name="assign_marks"),
    path('academic_students/<int:academic_id>/', views.StudentsByAcademic.as_view(), name="students_by_academics")
]
