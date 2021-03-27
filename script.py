import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_vacancies.settings'
django.setup()

from vacancy.models import Vacancy, Company, Specialty
from vacancy.data import jobs, companies, specialties

if __name__ == 'main':
    # for job in jobs:
    #     vacancy = Vacancy.objects.create(
    #         title=job['title'],
    #         specialty=job['specialty'],
    #         company=job['company'],
    #         skills=job['skills'],
    #         description=job['description'],
    #         salary_min=job['salary_from'],
    #         salary_max=job['salary_to'],
    #         published_at=job['posted'],
    #     )
    #
    # for company in companies:
    #     comp = Company.objects.create

    v1 = Vacancy.objects.all()
    print(v1)
