from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('<int:report_id>/', views.report, name='report'),
    path('list/', views.report_list, name='list'),
]