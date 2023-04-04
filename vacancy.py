
import json

HH_FILE_NAME = "hh.json"
SJ_FILE_NAME = "sj.json"



class CountMixin:

    def __init__(self, fname):
        self.filename = fname

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(self.filename, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print(f"Файл {self.filename} не содержит список")
            return False
        for v in data:
            for key, value in v.items:
                print("{:<20} {:<10} ".format(key, value))
        return len(data)






class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """
    def __init__(self):
        super().__init__(SJ_FILE_NAME)

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass
