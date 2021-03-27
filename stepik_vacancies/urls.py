from django.contrib import admin
from django.urls import path

import vacancy.views as vacancy_views
from vacancy.views import custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', vacancy_views.Home, name='home'),
    path('vacancies/', vacancy_views.Vacancies, name='vacancies'),
    path('vacancies/cat/backend', vacancy_views.Specialty, name='specialty'),
    path('companies/345', vacancy_views.Company, name='company'),
    path('vacancies/22', vacancy_views.Vacancy, name='vacancy')
]
