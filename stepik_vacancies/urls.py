from django.contrib import admin
from django.urls import path

from vacancy.views import custom_handler404, custom_handler500, HomeView, VacancyView


handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('vacancies/', vacancy_views.Vacancies, name='vacancies'),
    # path('vacancies/cat/backend', vacancy_views.Specialty, name='specialty'),
    # path('companies/<int:comp_id>', vacancy_views.Company, name='company'),
    path('vacancies/22', VacancyView.as_view(), name='vacancy')
]
