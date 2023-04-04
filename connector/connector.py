
import os
from abc import ABC, abstractmethod
class Connector(ABC):
    """
    Класс коннектор к файлу, файл может быть в разных форматах
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    @staticmethod
    def check_file_exist(fname: str) -> bool:
        return os.path.isfile(fname)

    @staticmethod
    def delete_file(fname: str):
        os.remove(fname)

    @abstractmethod
    def create_empty_file(self):
        """
        Пересоздаёт пустой файл
        """
        pass

    @abstractmethod
    def check_file_content(self):
        """
        Проверяет корректность содержимого файла
        """
        pass

    def check_file_exist_and_ok(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        ret = Connector.check_file_exist(self.fname)
        if not Connector.check_file_exist(self.fname):
            print(f"Нет такого файла {self.fname}. Будет создан новый файл.")
            self.create_empty_file()
        else:
            if not self.check_file_content():
                print(f"Содержимое файла {self.fname} повреждено. Будет создан новый файл.")
                self.create_empty_file()

    def __init__(self, fname: str):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        self.fname = fname
        self.file = None
        self.check_file_exist_and_ok()

