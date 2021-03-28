
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

from vacancy.models import Vacancy, Company, Specialty


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


class HomeView(TemplateView):
    template_name = 'vacancy/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Джуманджи'
        context['specialties'] = Specialty.objects.all()
        context['companies'] = Company.objects.all()
        return context


class SpecialtyView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancies.html'
    context_object_name = 'Vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Вакансии | Джуманджи'
        context['specialty'] = get_object_or_404(Specialty, code=self.kwargs['spec'])
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['spec']).select_related('specialty')


class VacanciesView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancies.html'
    context_object_name = 'Vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Вакансии | Джуманджи'
        context['specialty'] = {'title': 'Все вакансии'}
        return context


class CompanyView(ListView):
    model = Company
    template_name = 'vacancy/company.html'
    context_object_name = 'Company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Компания | Джуманджи'
        context['vacancies'] = Vacancy.objects.filter(company=self.kwargs['comp_id'])
        return context

    def get_queryset(self):
        return get_object_or_404(Company, pk=self.kwargs['comp_id'])


class VacancyView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy.html'
    context_object_name = 'Vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Вакансия | Джуманджи'
        return context

    def get_queryset(self):
        return get_object_or_404(Vacancy, pk=self.kwargs['vac_id'])
