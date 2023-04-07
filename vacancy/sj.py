
from vacancy.vacancy import Vacancy, VacancyCollection


class SJVacancy(Vacancy):
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'SJVacancy:("{self.name}", "{self.company}")'


