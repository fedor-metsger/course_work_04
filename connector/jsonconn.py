
import json
from connector import Connector

class JSONConnector(Connector):
    def create_empty_file(self):
        """
        Пересоздаёт пустой файл
        """
        with open(self.fname, "w", encoding="utf-8") as f:
            json.dump({}, f)

    def check_file_content(self):
        try:
            with open(self.fname, "r", encoding="utf-8") as f:
                json.load(f)
            return True
        except json.decoder.JSONDecodeError:
            return False

def main():
    json1 = JSONConnector("test.json")

if __name__ == "__main__":
    main()
