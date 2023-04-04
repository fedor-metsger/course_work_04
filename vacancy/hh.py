
from vacancy.vacancy import Vacancy

class HHVacancy(Vacancy):
    """ HeadHunter Vacancy """
    def __init__(self, id: str, name: str, company:str, url: str,
                 descr: str, sal_fr:int, sal_to: int, curr: str, site: str):

        Vacancy.__init__(self, name, company, url, descr, sal_fr, sal_to, curr)
        self.site = site

    def __str__(self):
        return f'HHVacancy:("{self.site}", "{self.name}", "{self.company}")'

    def __dict__(self):
        dic = Vacancy.__dict__()
        dic["site"] = self.site
        return dic