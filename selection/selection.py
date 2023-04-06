
SITE_HH = 1
SITE_SJ = 2

ACT_DOWNLOAD = 1
ACT_SELECT_FSAL = 2
ACT_SELECT_TSAL = 3
ACT_SELECT_REG = 4
ACT_SELECT_KW = 5
ACT_SELECT_ALL = 6

FTYPE_JSON = 1
FTYPE_YAML = 2

REG_MOSCOW = 1
REG_SPB = 2
REG_OTHER = 3

class Region():
    """
    Класс описывает регион
    """
    def __init__(self):
        self.region = REG_MOSCOW

    def select(self):
        """
        Запрашивает у пользователя регион
        :return:
        """

class UserSelection()
    """
    Класс описывает операцию, которую хочет выполнить пользователь
    """
    __init__