
class Vacancy:

    def __init__(self, id: str, name: str, company:str, url: str,
                 descr: str, sal_fr:int, sal_to: int, curr: str):

        if not isinstance(id, str) or id == "":
            raise ValueError("ID вакансии должно быть непустой строкой")
        if not isinstance(name, str) or name == "":
            raise ValueError("Название вакансии должно быть непустой строкой")
        if not isinstance(company, str) or company == "":
            raise ValueError("Название компании должно быть непустой строкой")
        if not isinstance(url, str) or url == "":
            raise ValueError("URL вакансии должен быть непустой строкой")
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

    def to_dict(self):
        data = {}
        for i in self.__vacancies:
            data[i] = self.__vacancies[i]
        return data


