
class Vacancy:

    def __init__(self, id: str, name: str, company:str, url: str,
                 descr: str, sal_fr:int, sal_to: int, curr: str):
        if not id or id == "":
            raise ValueError("ID вакансии не может быть пустым")
        if not name or id == "":
            raise ValueError("Название вакансии не может быть пустым")
        if not company or company == "":
            raise ValueError("Название компании не может быть пустым")
        if not url or url == "":
            raise ValueError("URL вакансии не может быть пустым")
        self.id = id
        self.name = name
        self.url = url
        self.descr = descr
        self.sal_fr = sal_fr
        self.sal_to = sal_to
        self.curr = curr
        self.company = company

    def __str__(self):
        return f'Vacancy("{self.name}", "{self.company}")'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "company": self.company, "url": self.url,
                "descr": self.descr, "sal_fr": self.sal_fr, "sal_to": self.sal_to, "curr": self.curr}

class VacancyCollection():
    def __init__(self):
        self.__vacancies = {}

    def __str__(self):
        return f'VacancyCollection({len(self.__vacancies)} vacancies)'

    def add_vacancy(self, vac: Vacancy) -> bool:
        if not isinstance(vac, Vacancy):
            raise TypeError("Можно добавлять только элементы типа Vacancy")
        if vac.id in self.__vacancies:
            raise ValueError("Вакансия с таким ID уже загружена")
        self.__vacancies[vac.id] = vac.to_dict()

    def clear_vacancies(self):
        self.__vacancies = {}


