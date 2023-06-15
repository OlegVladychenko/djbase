from datetime import timedelta, date, datetime
import datetime

from trade.models import ExchangeRates


def get_colors(count):
    colors = [
        '#FF0000',
        '#800000',
        '#FFFF00',
        '#808000',
        '#00FF00',
        '#008000',
        '#00FFFF',
        '#008080',
        '#0000FF',
        '#000080',
        '#FF00FF'
    ]
    return colors[:count]


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


def get_array_date_between(start_date, end_date):
    result = []
    for dt in date_range(start_date, end_date):
        result.append(dt.strftime("%Y%m%d"))
    return result

def load_exchange_rates_currencie(code_currencie):
    start_date = datetime.date(2022, 1, 1)
    last_ten = ExchangeRates.objects.filter(currencie_id=code_currencie).order_by('-id')[:1]
    if last_ten.count() > 0:
     start_date = last_ten[0].date



