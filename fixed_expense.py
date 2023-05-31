
class Fixed_expense:

    def __init__(self, reason, sum_E, payment_method):
        self._reason = reason
        self._sum_E = sum_E
        self._payment_method = payment_method

    def get_sum(self):
        return self._sum_E

    def __str__(self):
        return "Fixed_expense[\n\treason: {}\n\tsum_FE: {}\n\tpayment_method: {}]".format(self._reason, self._sum_E, self._payment_method)
