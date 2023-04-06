
import utils

SEL_SITES = {
    1: {"name": "HeadHunter"},
    2: {"name": "SuperJob"}
}

SEL_ACTIONS = {
    1: {"action": "DOWNLOAD", "name": "Загрузить вакансии с сайта в файл"},
    2: {"action": "SELECT", "name": "Выбрать вакансии из файла"},
    3: {"action": "EXIT", "name": "Завершить работу"}
}

SEARCH_TYPES = {
    1: {"stype": "FROM_SAL", "name": "Вакансии с максимальной нижней границей заработной платы"},
    2: {"stype": "TO_SAL", "name": "Вакансии с максимальной верхней границей заработной платы"},
    3: {"stype": "ALL", "name": "Все вакансии"}
}

SEL_FTYPES = {
    1: {"name": "JSON"},
    2: {"name": "YAML"}
}

SEL_REGIONS = {
    1: {"name": "Москва", "hh_code": 1},
    2: {"name": "Санкт-Петербург", "hh_code": 2},
    3: {"name": "Остальные", "hh_code": None}
}


def select_from_dict(prompt: str, val: int, dic: dict):
    """
    Запрашивает у пользователя сделать выбор из нескольких вариантов
    :return:
    """
    while True:
        print(f'{prompt} ({val}):')
        for i in dic.keys():
            print(f'{i}. {dic[i]["name"]}')
        i = input("=> ")
        if i == '': return val
        if not utils.contains_number(i) or not int(i) in dic:
            print("Некорректный ввод, попробуйте ещё..")
            continue
        return int(i)

class SelectionSite():
    """
    Класс описывает тип файла для вывода данных
    """
    def __init__(self):
        self.site = list(SEL_SITES.keys())[0]
        return

    def __str__(self):
        return f'SelectionSite("{self.site}")'

    def select(self):
        """
        Запрашивает у пользователя тип файла
        :return:
        """
        self.site = select_from_dict("Введите сайт для поиска", self.site, SEL_SITES)
        return self.site

class SelectionSearchType():
    """
    Класс описывает тип файла для вывода данных
    """
    def __init__(self):
        self.stype = list(SEARCH_TYPES.keys())[0]
        return

    def __str__(self):
        return f'SelectionFType("{self.stype}")'

    def select(self):
        """
        Запрашивает у пользователя тип файла
        :return:
        """
        self.stype = select_from_dict("Введите тип поиска вакансий", self.stype, SEARCH_TYPES)
        return self.stype

class SelectionAction():
    """
    Класс описывает тип файла для вывода данных
    """
    def __init__(self):
        self.action = list(SEL_ACTIONS.keys())[0]
        return

    def __str__(self):
        return f'SelectionFType("{self.action}")'

    def select(self):
        """
        Запрашивает у пользователя тип файла
        :return:
        """
        self.action = select_from_dict("Выберите действие", self.action, SEL_ACTIONS)
        return self.action

class SelectionFType():
    """
    Класс описывает тип файла для вывода данных
    """
    def __init__(self):
        self.ftype = list(SEL_FTYPES.keys())[0]
        return

    def __str__(self):
        return f'SelectionFType("{self.ftype}")'

    def select(self):
        """
        Запрашивает у пользователя тип файла
        :return:
        """
        self.ftype = select_from_dict("Выберите тип файла", self.ftype, SEL_FTYPES)
        return self.ftype
class SelectionRegion():
    """
    Класс описывает регион
    """
    def __init__(self):
        self.region = list(SEL_REGIONS.keys())[0]
        return

    def __str__(self):
        return f'SelectionRegion("{self.region}")'

    def select(self):
        """
        Запрашивает у пользователя регион
        :return:
        """
        self.region = select_from_dict("Выберите регион", self.region, SEL_REGIONS)
        return self.region

class UserSelection():
    """
    Класс описывает операцию, которую хочет выполнить пользователь
    """
    def __init__(self):
        self.site = SelectionSite()
        self.stype = SelectionSearchType()
        self.action = SelectionAction()
        self.region = SelectionRegion()
        self.ftype = SelectionFType()
        self.record_quant = 10
        self.key_word = ""

    def __str__(self):
        return f'UserSelection({self.site.site}, {self.action.action}, ' \
               f'{self.stype.stype}, {self.region.region}, {self.ftype.ftype}, {self.record_quant})'

    def select_quant(self, defq):
        while True:
            q = input(f"Введите количество вакансий ({defq}) => ")
            if q == '': return defq
            if not utils.contains_number(q) or int(q) < 1:
                print("Некорректный ввод, попробуйте ещё..")
                continue
            return int(q)

    def select_keyword(self, kw):
        return input(f"Введите ключевое слово или несколько слов, разделённых пробелом => ")

    def select_search(self):
        while True:
            kw_test = "без использования ключевого слова" if self.key_word == '' else \
                      f'с использованием ключевого слова "{self.key_word}"'
            region_text = "без учёта региона" if SEL_REGIONS[self.region.region]["hh_code"] == None else \
                      f'по региону {SEL_REGIONS[self.region.region]["name"]}'
            print(f'Из данных по сайту {SEL_SITES[self.site.site]["name"]} ' \
                  f'будут отбираться {SEARCH_TYPES[self.stype.stype]["name"].lower()}\n' \
                  f'{region_text} ' \
                  f'в количестве {self.record_quant} {kw_test}. Изменить запрос (6)?')
            print("\t1. Изменить сайт\n\t2. Изменить условие выбора вакансий\n\t3. Изменить количество вакансий\n" \
                  "\t4. Изменить ключевое слово\n\t5. Изменить регион\n\t6. Оставить как есть." )
            i = input("=> ")
            if i == '': return
            if not utils.contains_number(i) or int(i) not in {1, 2, 3, 4, 5, 6}:
                print("Некорректный ввод, попробуйте ещё..")
                continue
            if i == '1': self.site.select()
            if i == '2': self.stype.select()
            if i == '3': self.record_quant = self.select_quant(self.record_quant)
            if i == '4': self.key_word = self.select_keyword(self.key_word)
            if i == '5': self.region.select()
            if i == '6': return

    def select_action(self):
        self.action.select()
        if SEL_ACTIONS[self.action.action]["action"] == "DOWNLOAD":
            self.site.select()
            self.ftype.select()
        if SEL_ACTIONS[self.action.action]["action"] == "SELECT":
            self.ftype.select()
            self.select_search()


def main():
    # r = SelectionRegion()
    # r = SelectionFType()
    # r = SelectionAction()
    # r = SelectionSearchType()
    # r = SelectionSite()
    # r.select()
    # print(r)
    us = UserSelection()
    us.select_action()
    print(us)

if __name__ == "__main__":
    main()