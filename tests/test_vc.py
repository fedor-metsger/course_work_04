
import pytest
from vacancy.vacancy import Vacancy, VacancyCollection
from selection.selection import UserSelection

@pytest.fixture
def vac_a():  # имя фикстуры любое
    return Vacancy("111", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=111",
                   "Много работать", 20000, 30000, "RUR")


@pytest.fixture
def vac_b():  # имя фикстуры любое
    return Vacancy("222", "Инженер", "Завод", "https://www.hh.ru/vacancy?id=222",
                   "Много работать", 30000, 40000, "RUR")

@pytest.fixture
def vc():
    return VacancyCollection()

def test_init(vc):
    assert vc.vacancies == {}


def test_add_vacancy1(vac_a, vac_b, vc):
    vc.add_vacancy(vac_a)
    assert vc.vacancies[vac_a.id] == vac_a

def test_add_vacancy2(vc):
    with pytest.raises(TypeError):
        vc.add_vacancy(100)

def test_add_vacancy3(vac_a, vc):
    vc.add_vacancy(vac_a)
    with pytest.raises(ValueError):
        vc.add_vacancy(vac_a)

def test_str(vac_a, vc):
    vc.add_vacancy(vac_a)
    assert str(vc) == "VacancyCollection(1 vacancies)"

def test_clear(vac_a, vc):
    vc.add_vacancy(vac_a)
    vc.clear_vacancies()
    assert vc.vacancies == {}

def test_to_dict(vac_a, vc):
    vc.add_vacancy(vac_a)
    assert vc.to_dict() == {"111": vac_a.to_dict()}

def test_select(vac_a, vac_b, vc):
    vc.add_vacancy(vac_a)
    vc.add_vacancy(vac_b)
    sel = vc.select_vacancies(UserSelection())
    assert isinstance(sel, list) and len(sel) == 2