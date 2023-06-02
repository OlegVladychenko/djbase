from datetime import timedelta, date


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
