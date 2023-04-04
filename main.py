
import requests
from pprint import pprint
from connector import Connector, HHConnector, SJConnector
from vacancy import HHVacancy, SJVacancy, HH_FILE_NAME, SJ_FILE_NAME

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


def download_hh_to_file(kw:str):
    """
    Производит загрузку данных с сайта hh.ru
    :param kw:
    :return:
    """
    print("Выполняется загрузка вакансий с сайта HeadHunter по ключевому слову", kw)
    # headers = {
    #     "User-Agent": " CourseWork04/1.0 (fedor.metsger@gmail.com)"
    # }
    url = "https://api.hh.ru/vacancies"
    params = {
        'host': "hh.ru",
        "text": kw,
        "page": 0,
        "per_page": 100
    }
    res = []
    try:
        response = requests.get(url, params=params)
        for i in response.json()["items"]:
            # print(i["id"])
            company, descr, salary = None, None, None
            if isinstance(i["employer"], dict): company = i["employer"]["name"]
            if isinstance(i["snippet"], dict): descr = i["snippet"]["responsibility"]
            if isinstance(i["salary"], dict): salary = i["salary"]["from"]
            # res.append(HHVacancy(i["name"], i["employer"]["name"], i["url"], i["snippet"]["responsibility"], i["salary"]["from"]))
            res.append({"name":i["name"], "company": company, "url": i["url"], "descr": descr, "salary": salary})
    except Exception as e:
        print("Ошибка при запросе данных с сайта HeadHunter:", repr(e))

    if len(res) > 0:
        Connector.delete_file(HH_FILE_NAME)
        conn = HHConnector()
        conn.insert(res)

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
            try:
                hh = HHConnector()
            except Exception as e:
                print(f"Ошибка при чтении файла: {repr(e)}")
        elif i == '4':
            try:
                hh = SJConnector()
            except Exception as e:
                print(f"Ошибка при чтении файла: {repr(e)}")
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

