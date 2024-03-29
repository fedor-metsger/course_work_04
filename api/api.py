
from abc import ABC, abstractmethod
from vacancy.vacancy import Vacancy, VacancyCollection
from connector.connector import Connector

class Engine(ABC):

    def __init__(self, conn: Connector):
        self.data = VacancyCollection()
        self.connector = conn

    @abstractmethod
    def download_vacancies(self, kw: str) -> bool:
        """
        Осуществляет загрузку данных с сайта.
        Данные загружаются по ключевым словам
        :param kw: ключевые слова через пробел
        :return:
        """
        pass

    @abstractmethod
    def save_vacancies(self):
        """
        Осуществляет сохранение данных в файл
        :param:
        :return:
        """
    def save_vacancies(self):
        """
        Записывает данные, которые были загружены с сайта, в локальный файл.
        Та информация, что уже была в файле - не теряется.
        :return:
        """
        dict = self.connector.load_from_file()
        dict.update(self.data.to_dict())
        self.connector.dump_to_file(dict)




