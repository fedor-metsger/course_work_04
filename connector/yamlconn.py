
import yaml
from connector.connector import Connector

class YAMLConnector(Connector):
    def create_empty_file(self):
        """
        Пересоздаёт пустой файл
        """
        with open(self.fname, "w", encoding="utf-8") as f:
            yaml.dump({}, f, allow_unicode=True, default_flow_style=False)

    def check_file_content(self):
        """
        Проверяет содержимое файла с данными
        :return:
        """
        try:
            with open(self.fname, "r", encoding="utf-8") as f:
                yaml.load(f, Loader=yaml.FullLoader)
            return True
        except yaml.YAMLError:
            return False

    def dump_to_file(self, data: dict):
        """
        Записывает данные в файл
        """
        with open(self.fname, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

    def load_from_file(self) -> dict:
        """
        Забирает данные из файла
        """
        with open(self.fname, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

def main():
    yaml1 = YAMLConnector("test.yaml")
    yaml1.dump_to_file({"a": 1, "b": 2, "c": 3})
    d = yaml1.load_from_file()
    print(d)

if __name__ == "__main__":
    main()
