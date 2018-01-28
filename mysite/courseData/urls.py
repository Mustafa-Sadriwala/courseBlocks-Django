from django.urls import path

from . import views

urlpatterns = [
               # ex: /courseData/
               path('', views.all, name='all'),
               # ex: /courseData/MATH/
               path('<subj>/', views.subj, name='subj'),
               # ex: /courseData/MATH/2419/
               path('<dept>/<int:class_num>/', views.course_data, name='course_data'),
               ]
