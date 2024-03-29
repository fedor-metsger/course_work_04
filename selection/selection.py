
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
    1: {"name": "Все", "hh_code": None},
    2: {"name": "Москва", "hh_code": 1},
    3: {"name": "Санкт-Петербург", "hh_code": 2}
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
        self.site = select_from_dict("Выберите сайт для поиска", self.site, SEL_SITES)
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
        self.stype = select_from_dict("Выберите тип поиска вакансий", self.stype, SEARCH_TYPES)
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
    def __init__(self, ):
        self._site = SelectionSite()
        self._stype = SelectionSearchType()
        self._action = SelectionAction()
        self._region = SelectionRegion()
        self._ftype = SelectionFType()
        self._record_quant = 10
        self._keyword = ""

    def __str__(self):
        return f'UserSelection({self._site.site}, {self._action.action}, ' \
               f'{self._stype.stype}, {self._region.region}, {self._ftype.ftype}, {self._record_quant})'

    @property
    def action(self):
        return SEL_ACTIONS[self._action.action]["action"]

    @property
    def site(self):
        return SEL_SITES[self._site.site]["name"]

    @property
    def ftype(self):
        return SEL_FTYPES[self._ftype.ftype]["name"]

    @property
    def stype(self):
        return SEARCH_TYPES[self._stype.stype]["stype"]

    @property
    def quantity(self):
        return self._record_quant

    @property
    def keyword(self):
        if self._keyword and self._keyword != '':
            return self._keyword
        return ''

    def select_quant(self, defq):
        while True:
            q = input(f"Введите количество вакансий ({defq}) => ")
            if q == '': return defq
            if not utils.contains_number(q) or int(q) < 1:
                print("Некорректный ввод, попробуйте ещё..")
                continue
            return int(q)

    def select_keyword(self, kw):
        self._keyword = input(f"Введите ключевое слово или несколько слов, разделённых пробелом => ")
        return self._keyword


    def select_search(self):
        while True:
            kw_test = "без использования ключевого слова" if self._keyword == '' else \
                      f'с использованием ключевого слова "{self._keyword}"'
            region_text = "без учёта региона" if SEL_REGIONS[self._region.region]["hh_code"] == None else \
                      f'по региону {SEL_REGIONS[self._region.region]["name"]}'
            print(f'Из файла с данными по сайту {SEL_SITES[self._site.site]["name"]} ' \
                  f'будут отбираться {SEARCH_TYPES[self._stype.stype]["name"].lower()}\n' \
                  f'{region_text} ' \
                  f'в количестве {self._record_quant} {kw_test}. Изменить запрос (5)?')
            print("\t1. Изменить сайт\n\t2. Изменить условие выбора вакансий\n\t3. Изменить количество вакансий\n" \
                  "\t4. Изменить ключевое слово\n\t5. Оставить как есть." )
            i = input("=> ")
            if i == '': return
            if not utils.contains_number(i) or int(i) not in {1, 2, 3, 4, 5}:
                print("Некорректный ввод, попробуйте ещё..")
                continue
            if i == '1': self._site.select()
            if i == '2': self._stype.select()
            if i == '3': self._record_quant = self.select_quant(self._record_quant)
            if i == '4': self._keyword = self.select_keyword(self._keyword)
            if i == '5': return

    def select_action(self):
        self._action.select()
        if self.action == "DOWNLOAD":
            self._site.select()
            self._ftype.select()
            self.select_keyword("")
        if self.action == "SELECT":
            self._ftype.select()
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