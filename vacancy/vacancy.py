
from selection.selection import UserSelection
class Vacancy:

    usd_rate, eur_rate = None, None

    def __init__(self, id: str, name: str, company:str, url: str,
                 descr: str, sal_fr:int, sal_to: int, curr: str):

        if not isinstance(id, str) or id == "":
            raise ValueError("ID вакансии должно быть непустой строкой")
        if not isinstance(name, str) or name == "":
            raise ValueError("Название вакансии должно быть непустой строкой")
        if not isinstance(company, str) or company == "":
            raise ValueError("Название компании должно быть непустой строкой")
        if not isinstance(url, str) or url == "":
            raise ValueError("URL вакансии должен быть непустой строкой")
        self.id = id
        self.name = name
        self.url = url
        self.descr = descr
        self.sal_fr = sal_fr
        self.sal_to = sal_to
        self.curr = curr
        self.company = company

    def __str__(self):
        return f'Vacancy("{self.name}", "{self.company}")'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "company": self.company, "url": self.url,
                "descr": self.descr, "sal_fr": self.sal_fr, "sal_to": self.sal_to, "curr": self.curr}

    @classmethod
    def get_usd_rate(self):
        """
        Получает курс доллара к рублю
        :return:
        """
        if self.usd_rate: return self.usd_rate
        self.usd_rate = 80
        return self.usd_rate

    @classmethod
    def get_eur_rate(self):
        """
        Получает курс евро к рублю
        :return:
        """
        if self.eur_rate: return self.eur_rate
        self.eur_rate = 90
        return self.eur_rate

    @staticmethod
    def _convert_curr(sal, curr):
        if sal is None or sal == 0: return 0
        if curr == "USD": sal *= Vacancy.get_usd_rate()
        if curr == "EUR": sal *= Vacancy.get_eur_rate()
        return sal

    def __gt__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr > other_sal_fr

    def __ge__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr >= other_sal_fr

    def __lt__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr < other_sal_fr

    def __le__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr <= other_sal_fr

    def __eq__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr == other_sal_fr

    def __ne__(self, other) -> bool:
        """
        Сравнивает два класса Vacancy. Сравнение идёт по минимальной заработной плате
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        self_sal_fr = self._convert_curr(self.sal_fr, self.curr)
        other_sal_fr = self._convert_curr(other.sal_fr, other.curr)
        return self_sal_fr != other_sal_fr

class VacancyCollection():
    def __init__(self):
        self.__vacancies = {}

    def __str__(self):
        return f'VacancyCollection({len(self.__vacancies)} vacancies)'

    def add_vacancy(self, vac: Vacancy) -> bool:
        """
        Добавляет вакансию в коллекцию
        :param vac:
        :return:
        """
        if not isinstance(vac, Vacancy):
            raise TypeError("Можно добавлять только элементы типа Vacancy")
        if vac.id in self.__vacancies:
            raise ValueError("Вакансия с таким ID уже загружена")
        # self.__vacancies[vac.id] = vac.to_dict()
        self.__vacancies[vac.id] = vac

    def clear_vacancies(self):
        """
        Очищает коллекцию
        :return:
        """
        self.__vacancies = {}

    def to_dict(self):
        """
        Возвращает содержимое коллекции в виде словаря
        :return:
        """
        data = {}
        for i in self.__vacancies:
            data[i] = self.__vacancies[i]
        return data

    def select_vacancies(self, us: UserSelection):
        """
        возвращает необходимое количество вакансий отсортированных и отобранных
        в соответствии с пользовательским выбором
        :param us:
        :return:
        """
        data = []
        if us.stype == "FROM_SAL":
            data = sorted(self.__vacancies.values())

        return data[:us.quantity]

