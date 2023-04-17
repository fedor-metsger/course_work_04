import pytest
from vacancy.vacancy import Vacancy


@pytest.fixture
def vac_a():  # имя фикстуры любое
    return Vacancy("111", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=111",
                   "Много работать", 20000, 30000, "RUR")


@pytest.fixture
def vac_b():  # имя фикстуры любое
    return Vacancy("222", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=222",
                   "Много работать", 30000, 40000, "RUR")


def test_init1(vac_a):
    assert vac_a.id == "111"
    assert vac_a.name == "Инженер"
    assert vac_a.url == "https://www.hh.ru/vacancy?id=111"
    assert vac_a.descr == "Много работать"
    assert vac_a.sal_fr == 20000
    assert vac_a.sal_to == 30000
    assert vac_a.curr == "RUR"
    assert vac_a.company == "Завод"


def test_init2():
    with pytest.raises(TypeError):
        Vacancy(111, "Инженер", "Завод", "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init3():
    with pytest.raises(TypeError):
        Vacancy("111", None, "Завод", "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init4():
    with pytest.raises(TypeError):
        Vacancy("111", "Инженер", None, "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init5():
    with pytest.raises(TypeError):
        Vacancy("111", "Инженер", "Завод", None,
                "Много работать", 20000, 30000, "RUR")


def test_init6():
    with pytest.raises(ValueError):
        Vacancy("", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init7():
    with pytest.raises(ValueError):
        Vacancy("111", "", "Завод", "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init8():
    with pytest.raises(ValueError):
        Vacancy("111", "Инженер", "", "https://www.hh.ru/vacancy?id=111",
                "Много работать", 20000, 30000, "RUR")


def test_init9():
    with pytest.raises(ValueError):
        Vacancy("111", "Инженер", "Завод", "",
                "Много работать", 20000, 30000, "RUR")


def test_str(vac_a):
    assert str(vac_a) == 'Vacancy("Инженер", "20000" "RUR", "Завод")'


def test_to_dict(vac_a):
    assert vac_a.to_dict() == {'company': 'Завод',
                               'curr': 'RUR',
                               'descr': 'Много работать',
                               'id': '111',
                               'name': 'Инженер',
                               'sal_fr': 20000,
                               'sal_to': 30000,
                               'url': 'https://www.hh.ru/vacancy?id=111'}


def test_curr_rate(vac_a):
    Vacancy.get_curr_rate("KZT")
    assert Vacancy.rates["USD"]
    assert Vacancy.rates["EUR"]
    assert Vacancy.rates["BYN"]


def test_convert():
    assert Vacancy._convert_curr(100, "USD") == int(100 / Vacancy.get_curr_rate("USD"))
    assert Vacancy._convert_curr(None, "RUR") == 0
    assert Vacancy._convert_curr(1000, "RUB") == 1000


def test_gt(vac_a, vac_b):
    assert vac_b > vac_a
    assert (vac_a > vac_b) == False
    with pytest.raises(TypeError):
        vac_a > 20000


def test_ge(vac_a, vac_b):
    assert vac_b >= vac_a
    assert (vac_a >= vac_b) == False
    with pytest.raises(TypeError):
        vac_a >= 20000


def test_lt(vac_a, vac_b):
    assert vac_a < vac_b
    assert (vac_b < vac_a) == False
    with pytest.raises(TypeError):
        vac_a < 20000


def test_le(vac_a, vac_b):
    assert vac_a <= vac_b
    assert (vac_b <= vac_a) == False
    with pytest.raises(TypeError):
        vac_a <= 20000


def test_eq(vac_a, vac_b):
    assert (vac_b == vac_a) == False
    with pytest.raises(TypeError):
        vac_a == 20000


def test_ne(vac_a, vac_b):
    assert vac_a != vac_b
    with pytest.raises(TypeError):
        vac_a != 20000


def test_match(vac_a):
    assert vac_a.match_kw("Завод")
    assert vac_a.match_kw("Инженер")
    assert vac_a.match_kw("работать")
    assert vac_a.match_kw("завод инженер работать")
    assert vac_a.match_kw("Фабрика") == False
    assert vac_a.match_kw("Фабрика инженер")

def test_conv_sal_to(vac_a):
    assert vac_a.converted_sal_to == 30000

