
import requests
from pprint import pprint
from connector import Connector, HHConnector, SJConnector

def ask_user_input():
    """
    Выводит на экран меню с возможными операциями, спрашивает и возвращает пользовательский выбор
    :return:
    """
    while True:
        print("Выберите действие (1):\n\t1. Загрузить вакансии HeadHunter с сайта в файл.\n" +
              "\t2. Загрузить вакансии SuperJob с сайта в файл.\n" +
              "\t3. Выбрать вакансии из файла HeadHunter.\n" +
              "\t4. Выбрать вакансии из файла SuperJob.\n" +
              "\t6. Завершить работу.")
        i = input("=> ")
        if i == '' or i == '1':
            kw = input("Введите ключевое слово для поиска вакансий (python): ")
            return '1', kw if kw != "" else "python"
        elif i == '2':
            kw = input("Введите ключевое слово для поиска вакансий (python): ")
            return '2', kw if kw != "" else "python"
        elif i == '3' or i == '4':
            return i, None
        elif i == '6':
            return '6', None
        else:
            print("Некорректный ввод, попробуйте ещё..")

def save_hh_to_file():
    pass

def download_hh_to_file(kw:str):
    """
    Производит загрузку данных с сайта hh.ru
    :param kw:
    :return:
    """
    print("Выполняется загрузка вакансий с сайта HeadHunter по ключевому слову", kw)

    # token = ""
    # params = {
    #     'host': "hh.ru",
    #     "text": "python"
    # }
    #
    # headers = {
    #     "User-Agent": " CourseWork04/1.0 (fedor.metsger@gmail.com)"
    # }
    #
    # url = "https://api.hh.ru/vacancies"
    # response = requests.get(url, params=params)
    # pprint(response.json())

def download_sj_to_file(kw:str):
    """
    Производит загрузку данных с сайта superjob.ru
    :param kw:
    :return:
    """
    print("Выполняется загрузка вакансий с сайта SuperJob по ключевому слову", kw)

def main():
    while True:
        (i, kw) = ask_user_input()
        if i == '' or i == '1': download_hh_to_file(kw)
        elif i == '2': download_sj_to_file(kw)
        elif i == '3':
            hh = HHConnector()
        elif i == '4':
            hh = SJConnector()
        elif i == '6': return

    # token = ""
    # params = {
    #     'host': "hh.ru",
    #     "text": "python"
    # }
    #
    # headers = {
    #     "User-Agent": " CourseWork04/1.0 (fedor.metsger@gmail.com)"
    # }
    #
    # url = "https://api.hh.ru/vacancies"
    # response = requests.get(url, params=params)
    # pprint(response.json())


if __name__ == "__main__":
    main()

