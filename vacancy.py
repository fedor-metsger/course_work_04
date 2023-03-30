

HH_FILE_NAME = "hh.json"
SJ_FILE_NAME = "sj.json"

class Vacancy:
    __slots__ = ("name", "url", "descr", "salary", "company")

    def __init__(self, name: str, company:str, url: str, descr: str, salary:int):
        self.name = name
        self.url = url
        self.descr = descr
        self.salary = salary
        self.company = company

    def __str__(self):
        return f'Vacancy("{self.name}")'
    def __repr__(self):
        return f'Vacancy("{self.name}", "{self.company}", "{self.salary}", "{self.url}")'



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass
