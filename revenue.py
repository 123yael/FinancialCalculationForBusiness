
from datetime import date

class Revenue:

    def __init__(self, date_R, num_R, client, reason, sum_R):
        self._date_R = date_R
        self._num_R = num_R
        self._client = client
        self._reason = reason
        self._sum_R = sum_R

    def get_date(self):
        date1 = list(map(int, self._date_R.split("/")))
        return date(date1[2], date1[1], date1[0])

    def get_sum(self):
        return self._sum_R

    def get_num_R(self):
        return self._num_R

    def __str__(self):
        return "Revenue[\n\tdate_R: {}\n\tnum_R: {}\n\tclient: {}\n\treason: {}\n\tsum_R: {}]".format(
            self._date_R, self._num_R, self._client, self._reason, self._sum_R)
