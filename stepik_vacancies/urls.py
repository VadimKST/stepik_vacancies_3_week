from django.urls import path, include

from stepik_vacancies import settings

from vacancy.views import (custom_handler404, custom_handler500, HomeView, VacancyView, SpecialtyView, VacanciesView,
                           CompanyView)

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:spec>', SpecialtyView.as_view(), name='specialty'),
    path('companies/<int:comp_id>', CompanyView.as_view(), name='company'),
    path('vacancies/<int:vac_id>', VacancyView.as_view(), name='vacancy'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
