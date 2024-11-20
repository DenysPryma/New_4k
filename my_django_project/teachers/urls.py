from django.urls import path
from teachers.views import loadList, LoadDetail
from teachers.views import TeachersList, TeachersDetail

urlpatterns = [
    path('api/v1/load/', loadList.as_view(), name='load_list'),
    path('api/v1/load//<int:pk>/', LoadDetail.as_view(), name='load_detail'),
    path('api/v1/teachers/', TeachersList.as_view(), name='teachers_list'),
    path('api/v1/teachers//<int:pk>/', TeachersDetail.as_view(), name='teachers_detail'),
]