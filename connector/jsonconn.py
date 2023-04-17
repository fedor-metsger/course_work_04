
import json
from connector.connector import Connector

class JSONConnector(Connector):
    def create_empty_file(self):
        """
        Пересоздаёт пустой файл
        """
        with open(self.fname, "w", encoding="utf-8") as f:
            json.dump({}, f)

    def check_file_content(self):
        """
        Проверяет содержимое файла данных
        :return:
        """
        try:
            with open(self.fname, "r", encoding="utf-8") as f:
                json.load(f)
            return True
        except json.decoder.JSONDecodeError:
            return False

    def dump_to_file(self, data: dict):
        """
        Записывает данные в файл
        """
        with open(self.fname, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self) -> dict:
        """
        Забирает данные из файла
        """
        with open(self.fname, "r", encoding="utf-8") as f:
            return json.load(f)

def main():
    json1 = JSONConnector("test.json")
    json1.dump_to_file({"a": 1, "b": 2, "c": 3})
    d = json1.load_from_file()
    print(d)

if __name__ == "__main__":
    main()
