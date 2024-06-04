from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employee_view(request):
    employee = {
        'name':"ali Sultani",
        "sallay":100,
        "Education":"Bachelor"
    }
    return JsonResponse(employee)