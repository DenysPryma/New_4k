from django.urls import path
from departments.views import DepartmentsList,DepartmentsDetail

urlpatterns = [
    path('api/v1/depertments/', DepartmentsList.as_view(), name='depertments_list'),
    path('api/v1/depertments/<int:pk>/', DepartmentsDetail.as_view(), name='depertments_detail'),
]