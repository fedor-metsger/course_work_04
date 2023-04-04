
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