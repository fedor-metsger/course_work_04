
import Vacancy from vacancy.vacancy
class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __init__(self, name: str, company:str, url: str, descr: str, salary:int):
        Vacancy.__init__(self, name, company, url, descr, salary)
        CountMixin.__init__(self, HH_FILE_NAME)

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'