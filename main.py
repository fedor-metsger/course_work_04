
from connector.jsonconn import JSONConnector
from connector.yamlconn import YAMLConnector
from api.hh import HH
from api.sj import SJ
from selection.selection import UserSelection, SEL_ACTIONS, SEL_SITES, SEL_FTYPES
from vacancy.vacancy import VacancyCollection
from vacancy.hh import HHVacancy
from vacancy.sj import SJVacancy

def print_vacancies(data: dict):
    """
    Выводит список вакансий на экран красиво
    :param data: список вакансий
    :return:
    """
    print(f' Название вакансии         |     Название компании     |  Зарплата   |  Зарплата')
    print(f'                           |                           |     от      |     до')
    print(f'---------------------------|---------------------------|-------------|-------------')
    for v in data:
        sal_fr, sal_to = "Не указана", "Не указана"
        if v.sal_fr and v.curr and v.curr != '': sal_fr = str(v.sal_fr) + ' ' + v.curr
        elif v.sal_fr: sal_fr = str(v.sal_fr)
        if v.sal_to and v.curr and v.curr != '': sal_to = str(v.sal_to) + ' ' + v.curr
        elif v.sal_to: sal_fr = str(v.sal_to)
        print(" {:<25} | {:<25} | {:>11} | {:>11}".format(v.name[:25], v.company[:25], sal_fr, sal_to))

def main():
    us = UserSelection()
    while True:
        us.select_action()
        if us.action == "DOWNLOAD":
            print(f'Выполняется загрузка вакансий с сайта {us.site} ' \
                  f'в файл {us.ftype} ' \
                  f'по ключевому слову "{us.keyword}"')

            # if us.site() == "HeadHunter" and us.ftype() == "JSON":
            if us.site == "HeadHunter":
                api = HH("hh.ru", JSONConnector("hh.json") if us.ftype == "JSON" else YAMLConnector("hh.yaml"))
                # connector = JSONConnector("hh.json")
                # api = HH("hh.ru", connector)
            # elif us.site() == "HeadHunter" and us.ftype() == "YAML":
            #     connector = YAMLConnector("hh.yaml")
            #     api = HH("hh.ru", connector)
            elif us.site == "SuperJob":
                api = SJ(JSONConnector("sj.json") if us.ftype == "JSON" else YAMLConnector("sj.yaml"))

            else: return
            if api.download_vacancies(us.keyword):
                api.save_vacancies()
        elif us.action == "SELECT":
            fname = "hh." if us.site == "HeadHunter" else "sj."
            fname += "json" if us.ftype == "JSON" else "yaml"
            print(f'Выполняется выборка вакансий из файла {fname}')
            connector = JSONConnector(fname) if us.ftype == "JSON" else YAMLConnector(fname)
            vdict = connector.load_from_file()
            vc = VacancyCollection()
            for i in vdict.values():
                v = HHVacancy(**i) if us.site == "HeadHunter" else SJVacancy(**i)
                vc.add_vacancy(v)
            # for i in vc.select_vacancies(us):
            #     print(i)
            print_vacancies(vc.select_vacancies(us))
        elif us.action == "EXIT":
            return


if __name__ == "__main__":
    main()

