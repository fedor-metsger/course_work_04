
from vacancy import Vacancy, VacancyCollection

class HHVacancy(Vacancy):
    """ HeadHunter Vacancy """
    def __init__(self, id: str, name: str, company:str, url: str,
                 descr: str, sal_fr:int, sal_to: int, curr: str, site: str):

        Vacancy.__init__(self, id, name, company, url, descr, sal_fr, sal_to, curr)
        self.site = site

    def __str__(self):
        return f'HHVacancy:("{self.site}", "{self.name}", "{self.company}")'

    def __dict__(self):
        dic = Vacancy.__dict__()
        dic["site"] = self.site
        return dic


def main():
    vac1 = HHVacancy("111", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=111",
                     "Много работать", 20000, 30000, "RUR", "hh.ru")
    print(vac1)
    print(vac1.to_dict())
    coll1 = VacancyCollection()
    coll1.add_vacancy(vac1)
    print(coll1)


if __name__ == "__main__":
    main()