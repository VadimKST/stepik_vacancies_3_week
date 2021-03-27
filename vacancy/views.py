from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, Http404
from django.views.generic import ListView


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def Home(request):
    return render(request, 'vacancy/index.html')


def Vacancies(request):
    return render(request, 'vacancy/vacancies.html')


def Specialty(request):
    return render(request, 'vacancy/vacancies.html')


def Company(request):
    return render(request, 'vacancy/company.html')


def Vacancy(request):
    return render(request, 'vacancy/vacancy.html')