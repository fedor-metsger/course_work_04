
from pprint import pprint
import requests
from api.api import Engine
from vacancy.vacancy import VacancyCollection
from vacancy.sj import SJVacancy
from connector.connector import Connector
from connector.jsonconn import JSONConnector

PAGE_SIZE = 10

API_FILE_NAME = "sj_api_key.txt"
# API_KEY = "v3.r.137479983.d452e02a3a54ca2d71c13a0e5b6901887541f242.65a6dba4d80283fffeca51a08e74404541228624"

class SJ(Engine):
    def __init__(self, conn: Connector):
        Engine.__init__(self, conn)
        self.__api_key = None
        try:
            with open(API_FILE_NAME) as apifile:
                self.__api_key = apifile.readline()
            if not self.__api_key or self.__api_key == '':
                raise EOFError("Файл пустой")
        except Exception as e:
            print(f'Ошибка при чтении файла "{API_FILE_NAME}":\n' \
                  f'"{str(e)}"\n' \
                  "В первой строке файл должен содержать ключ доступа к API SuperJob")


    def __str__(self):
        return f'SJ({self.data})'

    def __download_vacancies_page(self, kw: str, pg: int):
        """
        Производит загрузку одной страницы данных с сайта hh.ru
        :param site: сайт
        :param kw: ключевые слова
        :param pg: номер страницы
        :return:
        """
        url = "https://api.superjob.ru/2.0/vacancies"
        headers = {
            "X-Api-App-Id": self.__api_key,
        }
        params = {
            "keyword": kw,
            "page": pg,
            "count": PAGE_SIZE
        }
        count, pages = 0, 0
        try:
            response = requests.get(url, params=params, headers=headers)
            if response.status_code != 200:
                print("Ошибка при запросе данных с сайта SuperJob: Status code ", response.status_code)
                return None, None

            pages = response.json()["total"] % PAGE_SIZE + 1
            # pprint(response.json())
            for i in response.json()["objects"]:
                id = i["id"]
                name = i["profession"]
                url = i["link"]
                company, descr, salary_from, salary_to, currency, city = None, None, None, None, None, None
                if isinstance(i["client"], dict): company = i["client"]["title"]
                descr = i["candidat"]
                if isinstance(i["town"], dict): city = i["town"]["title"]
                salary_from = i["payment_from"]
                salary_to = i["payment_to"]
                currency = i["currency"]

                print(id, name, salary_from, salary_to, currency, city, url)

                vac = SJVacancy(str(id), name, company, url,
                                descr, salary_from, salary_to, currency)
                self.data.add_vacancy(vac)
                count += 1
        except Exception as e:
            print("Ошибка при запросе данных с сайта SuperJob:", repr(e))
            return None, None

        return count, pages

    def download_vacancies(self, kw: str) -> bool:
        """
        Производит загрузку данных с сайта sj.ru
        :param site: сайт
        :param kw: ключевые слова
        :return:
        """
        if not isinstance(kw, str):
            raise ValueError("Ключевые слова должны задаваться строкой")

        print(f'Выполняется загрузка вакансий с сайта SuperJob c ключевыми словами "{kw}"')

        count, pg = 0, 0
        while True:
            ret, ret_pages = self.__download_vacancies_page(kw, pg)
            if not ret and count == 0: return False
            if self.data == None:
                print(f"Нет вакансий с такими ключевыми словами")
                return False
            pg += 1
            count += ret
            if pg == ret_pages:
                print(f'Загружено {count} вакансий')
                return True
            if count >= 20:
                print(f'Загрузка временно ограничена 20 вакансий. Загружено {count} вакансий')
                return True

    # def save_vacancies(self):
    #     dict = self.connector.load_from_file()
    #     dict.update(self.data.to_dict())
    #     self.connector.dump_to_file(dict)


def main():
    api = SJ(JSONConnector("test.json"))
    api.download_vacancies("Python")
    print(api)
    api.save_vacancies()

if __name__ == "__main__":
    main()