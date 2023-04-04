
from abc import ABC, abstractmethod
from vacancy.vacancy import Vacancy, VacancyCollection

class Engine(ABC):

    def __init__(self):
        self.data = VacancyCollection()

    @abstractmethod
    def download_vacancies(self, kw: str) -> bool:
        """
        Осуществляет загрузку данных с сайта.
        Данные загружаются по ключевым словам
        :param kw: ключевые слова через пробел
        :return:
        """
        pass

    # @abstractmethod
    def save_vacancies(self):
        """
        Осуществляет сохранение данных в файл
        :param:
        :return:
        """

    #
    # @abstractmethod
    # def load_vacancies(self):
    #     """
    #     Осуществляет чтение данных из файла
    #     :param:
    #     :return:
    #     """
    #     pass



