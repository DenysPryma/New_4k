from django.urls import path
from subjects.views import SubjectsList, SubjectsDetail

urlpatterns = [
    path('api/v1/subjects/', SubjectsList.as_view(), name='subjects_list'),
    path('api/v1/subjects//<int:pk>/', SubjectsDetail.as_view(), name='subjects_detail'),
]