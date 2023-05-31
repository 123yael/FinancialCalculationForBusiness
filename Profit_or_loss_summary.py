
from datetime import date

class Profit_or_loss_summary:

    def __init__(self, revenues_by_months, expenses_by_months, update_year):
        self._revenues_by_months = revenues_by_months
        self._expenses_by_months = expenses_by_months
        self._year = update_year
        self.calculation_of_profit_or_loss()

    def calculation_of_profit_or_loss(self):
        """
        Calculation of amount in loss or profit
        """
        sum_of_revenues = sum(list(self._revenues_by_months.values()))
        sum_of_expenses = sum(list(self._expenses_by_months.values()))
        result = sum_of_revenues - sum_of_expenses
        self._isProfit = result > 0
        self._sum = abs(result)

    def get_year(self):
        return self._year

    def set_expenses_by_months(self, r_date, sum_e):
        self._expenses_by_months[date(int(r_date[2]), int(r_date[1]), int(r_date[0])).strftime('%B')] += sum_e
        self.calculation_of_profit_or_loss()

    def set_revenues_by_months(self, r_date, sum_R):
        self._revenues_by_months[date(int(r_date[2]), int(r_date[1]), int(r_date[0])).strftime('%B')] += sum_R
        self.calculation_of_profit_or_loss()

    def get_revenues_by_months(self):
        return self._revenues_by_months

    def get_expenses_by_months(self):
        return self._expenses_by_months

    def get_sum(self):
        return self._sum

    def __str__(self):
        word = "loss"
        if self._isProfit:
            word = "profit"
        return "{}: {}".format(word, self._sum)
