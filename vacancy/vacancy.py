
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

    def __dict__(self):
        return {"id", self.id, "name": self.name, "url": self.url, "descr": self.descr,
                "sal_fr": self.sal_fr, "sal_to": self.sal_to, "curr": self.curr, "company": self.company}

class VacancyCollection():
    def __init__(self):
        self.vacancies = {}

    def add_vacancy(self, vac: Vacancy) -> bool:
        if not isinstance(vac, Vacancy):
            raise TypeError("Можно добавлять только элементы типа Vacancy")
        self.vacancies[vac.id] = dict(vac)