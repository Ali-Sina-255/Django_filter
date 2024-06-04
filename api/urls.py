from django.urls import path
from . import views
urlpatterns = [
    path('api/',views.employee_view,name='employee')
]
