
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
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
        return context

    def get_queryset(self):
        return Company.objects.value()
#
#
# class Vacancies(ListView):
#     model = Vacancy
#     template_name = 'vacancy/vacancies.html'
#     context_object_name = 'Vacancy'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Джуманджи'


# class Specialty(ListView):
#     model = Specialty
#     template_name = 'vacancy/index.html'
#     context_object_name = 'Specialty'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Джуманджи'


# class Company(ListView):
#     model = Company
#     template_name = 'vacancy/index.html'
#     context_object_name = 'Company'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Джуманджи'


class VacancyView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy.html'
    context_object_name = 'Vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Вакансия | Джуманджи'
        context['Vacancy'] = Vacancy.objects.get(pk=1)
        print(context)
        return context
    #
    # def get_queryset(self):
    #     return Vacancy.objects.filter(pk=self.kwargs['vac_id']).select_related('company')