
from vacancy.vacancy import Vacancy, VacancyCollection


class SJVacancy(Vacancy):
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJVacancy:("{self.name}", "{self.sal_fr}" "{self.curr}", "{self.company}")'


