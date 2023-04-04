

class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """
    def __init__(self):
        super().__init__(SJ_FILE_NAME)

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'
