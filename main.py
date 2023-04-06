
from pprint import pprint
from connector import Connector, HHConnector, SJConnector
from vacancy import HHVacancy, SJVacancy, HH_FILE_NAME, SJ_FILE_NAME
import selection.selection
import utils

def asl_selection_params() -> tuple:
    """
    Запрашивает у пользователя параметры поиска вакансий
    :return:
    """
    hh, st, rc, kw = True, ACT_SELECT_HH_FSAL, 10, "Flask"
    while True:
        print(f"Будет показано {rc} вакансий с сайта HeadHunter\n"с максимальной нижней заработной платой")


    j = input("Введите тип поиска вакансий (5).\n" +
              "\t1. По максимальной нижней границе заработной платы.\n" +
              "\t2. По максимальной верхней границе заработной платы.\n" +
              "\t3. По региону.\n" +
              "\t4. По ключевому слову\n" +
              "\t5. Все вакансии\n" +
              "=> ")
    if not j in {'1', '2', '3', '4', '5', ''}:
        print("Некорректный ввод, попробуйте ещё..")
        continue
    q = input("Введите количество вакансий для просмотра (10): ")
    if not contains_number(q):
        print("Некорректный ввод, попробуйте ещё..")
        continue
def ask_user_input() -> tuple:
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
            return ACT_DOWNLOAD_HH, kw if kw != "" else "python"
        elif i == '2':
            kw = input("Введите ключевое слово для поиска вакансий (python): ")
            return ACT_DOWNLOAD_SJ, kw if kw != "" else "python"
        elif i == '3' or i == '4':
            while True:
                j = input("Введите тип поиска вакансий (5).\n" +
                          "\t1. По максимальной нижней границе заработной платы.\n" +
                          "\t2. По максимальной верхней границе заработной платы.\n" +
                          "\t3. По региону.\n" +
                          "\t4. По ключевому слову\n" +
                          "\t5. Все вакансии\n" +
                          "=> ")
                if not j in {'1', '2', '3', '4', '5', ''}:
                    print("Некорректный ввод, попробуйте ещё..")
                    continue
                q = input("Введите количество вакансий для просмотра (10): ")
                if not contains_number(q):
                    print("Некорректный ввод, попробуйте ещё..")
                    continue
                if j == '1':
                    return ACT_SELECT_HH_FSAL if i == '3' else ACT_SELECT_SJ_FSAL, q
                if j == '2':
                    return ACT_SELECT_HH_TSAL if i == '3' else ACT_SELECT_SJ_TSAL, q
                if j == '3':

            return i, None
        elif i == '6':
            return '6', None
        else:
            print("Некорректный ввод, попробуйте ещё..")


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
        if i == '' or i == ACT_DOWNLOAD_HH: download_hh_to_file(kw)
        elif i == ACT_DOWNLOAD_SJ: download_sj_to_file(kw)
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

if __name__ == "__main__":
    main()

