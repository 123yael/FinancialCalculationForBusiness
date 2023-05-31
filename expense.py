
import fixed_expense as fe

from datetime import date

class Expense(fe.Fixed_expense):

    def __init__(self, date_E, reason, sum_E, payment_method):
        super().__init__(reason, sum_E, payment_method)
        self._date_E = date_E

    def __str__(self):
        return "Expense[\n\tdate_E: {}".format(self._date_E) + super().__str__()[14:]

    def get_date(self):
        date1 = list(map(int, self._date_E.split("/")))
        return date(date1[2], date1[1], date1[0])
