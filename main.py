
from connector.jsonconn import JSONConnector
from connector.yamlconn import YAMLConnector
from api.hh import HH
from selection.selection import UserSelection, SEL_ACTIONS, SEL_SITES, SEL_FTYPES

def main():
    us = UserSelection()
    while True:
        us.select_action()
        if SEL_ACTIONS[us.action.action]["action"] == "DOWNLOAD":
            print(f'Выполняется загрузка вакансий с сайта {SEL_SITES[us.site.site]["name"]} ' \
                  f'в файл {SEL_SITES[us.ftype.ftype]["name"]}' \
                  f'по ключевому слову "{us.key_word}"')

            if SEL_SITES[us.site.site]["name"] == "HeadHunter" and SEL_FTYPES[us.ftype.ftype]["name"] == "JSON":
                connector = JSONConnector("hh.json")
                api = HH("hh.ru", connector)
            elif SEL_SITES[us.site.site]["name"] == "HeadHunter" and SEL_FTYPES[us.ftype.ftype]["name"] == "YAML":
                connector = YAMLConnector("hh.yaml")
                api = HH("hh.ru", connector)
            else:
                return
            if api.download_vacancies(us.key_word):
                api.save_vacancies()
        elif SEL_ACTIONS[us.action.action]["action"] == "SELECT":
            us.select_search()
        elif SEL_ACTIONS[us.action.action]["action"] == "EXIT":
            return

if __name__ == "__main__":
    main()

