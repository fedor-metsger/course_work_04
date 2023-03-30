
import requests
from pprint import pprint

def ask_user():
    while True:
        print("Выберите действие (1):\n\t1. Загрузить вакансии HH с сайта в файл.\n" +
              "\t2. Загрузить вакансии SuperJob с сайта в файл.\n" +
              "\t3. Завершить работу.\n" +
            "=> ")
        i = input()
        if i == '1':
            kw = input("Введите ключевое слово для поиска вакансий (Python): ")
            return 1, kw
        elif i == '2':
            kw = input("Введите ключевое слово для поиска вакансий (Python): ")
            return 2, kw
        elif i == '3':
            return 3, None
        else:
            print("Некорректный ввод, попробуйте ещё..")

def load_hh_to_file(kw:str):
    print("Выполняется загрузка вакансий с сайта HeadHunter по ключевому слову", kw)

def load_sj_to_file(kw:str):
    print("Выполняется загрузка вакансий с сайта SuperJob по ключевому слову", kw)

def main():
    print("С богом!")

    while True:
        i, kw = ask_user()
        if i == '1':
            load_hh_to_file(kw)
        elif i == '2':
            load_sj_to_file(kw)
        elif i == '3':
            return

    token = ""
    params = {
        'host': "hh.ru",
        "text": "python"
    }

    headers = {
        "User-Agent": " CourseWork04/1.0 (fedor.metsger@gmail.com)"
    }

    url = "https://api.hh.ru/vacancies"
    response = requests.get(url, params=params)
    pprint(response.json())

    while True:
        print
        if
if __name__ == "__main__":
    main()

