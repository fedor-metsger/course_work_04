
from vacancy import Vacancy, HHVacancy, SJVacancy, HH_FILE_NAME, SJ_FILE_NAME

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        # тут должен быть код для установки файла
        if type(value) != "str":
            print("Имя файла должно быть строкой")
            return
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        try:
            vac = Vacancy(self.__data_file)
            count = vac.get_count_of_vacancy()
            if type(count) != "int":
                raise ValueError(f"Файл {self.__data_file} содержит неверный формат данных")
        except FileNotFoundError:
            try:
                self.file = open(self.__data_file, "w", encoding="utf-8")
                self.file.write("[]")
                self.file.close()
            except:
                print(f"Ошибка при создании файла {self.__data_file}")
                return False
        return count


    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        pass


    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        pass

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass

class HHConnector(Connector):
    def __init__(self):
        super().data_file = HH_FILE_NAME

class SJConnector(Connector):
    def __init__(self):
        super().__init__(SJ_FILE_NAME)
        super().__connect()

if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert([data_for_file])
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id':1})
    data_from_file = df.select(dict())
    assert data_from_file == []