
from connector.jsonconn import JSONConnector
from connector.yamlconn import YAMLConnector
from api.hh import HH
from api.sj import SJ
from selection.selection import UserSelection, SEL_ACTIONS, SEL_SITES, SEL_FTYPES
from vacancy.vacancy import VacancyCollection
from vacancy.hh import HHVacancy
from vacancy.sj import SJVacancy

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
            for i in vc.select_vacancies(us):
                print(i.)
        elif us.action == "EXIT":
            return


if __name__ == "__main__":
    main()

