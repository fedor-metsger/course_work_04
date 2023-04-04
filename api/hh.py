
import requests
from api import Engine
from vacancy.vacancy import VacancyCollection
from vacancy.hh import HHVacancy

PAGE_SIZE = 100

class HH(Engine):
    def __init__(self, site: str):
        Engine.__init__(self)
        self.site = site

    def __str__(self):
        return f'HH({self.data})'

    def __download_vacancies_page(self, kw: str, pg: int):
        """
        Производит загрузку одной страницы данных с сайта hh.ru
        :param site: сайт
        :param kw: ключевые слова
        :param pg: номер страницы
        :return:
        """
        url = "https://api.hh.ru/vacancies"
        params = {
            'host': self.site,
            "text": kw,
            "area": [1, 2],
            "page": pg,
            "per_page": PAGE_SIZE
        }
        count, pages = 0, 0
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print("Ошибка при запросе данных с сайта HeadHunter: Status code ", response.status_code)
                return None, None

            pages = response.json()["pages"]
            for i in response.json()["items"]:
                # print(i["id"])
                company, descr, salary_from, salary_to, currency, city = None, None, None, None, None, None
                if isinstance(i["employer"], dict): company = i["employer"]["name"]
                if isinstance(i["snippet"], dict): descr = i["snippet"]["responsibility"]
                if isinstance(i["area"], dict): city = i["area"]["name"]
                if isinstance(i["salary"], dict):
                    salary_from = i["salary"]["from"]
                    salary_to = i["salary"]["to"]
                    currency = i["salary"]["currency"]

                # res.append({"name": i["name"], "company": company, "url": i["url"],
                #             "salary_from": salary_from, "salary_to": salary_to, "currency": currency,
                #             "url": i["url"], "city": city})
                vac = HHVacancy(i["id"], i["name"], company, i["url"],
                                descr, salary_from, salary_to, currency, self.site)
                self.data.add_vacancy(vac)
                count += 1
        except Exception as e:
            print("Ошибка при запросе данных с сайта HeadHunter:", repr(e))
            return None, None

        return count, pages

    def download_vacancies(self, kw: str) -> bool:
        """
        Производит загрузку данных с сайта hh.ru
        :param site: сайт
        :param kw: ключевые слова
        :return:
        """
        print(f'Выполняется загрузка вакансий с сайта HeadHunter c ключевыми словами "{kw}"')

        count, pg = 0, 0
        while True:
            ret, ret_pages = self.__download_vacancies_page(kw, pg)
            if not ret: return False
            if self.data == None:
                print(f"Нет вакансий с такими ключевыми словами")
                return False
            pg += 1
            count += ret
            if pg == ret_pages:
                print(f'Загружено {count} вакансий')
                return True

def main():
    api = HH("hh.ru")
    api.download_vacancies("Flask Django")
    print(api)

if __name__ == "__main__":
    main()