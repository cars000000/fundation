import urllib3


def get_fundation_history(fund_id, start_date=None, end_date=None):
    url_prefix = "http://www.dayfund.cn/fundvalue/"
    url = url_prefix + fund_id

    if start_date is None:
        s_date = "2016-01-01"
    else:
        s_date = start_date

    if end_date is None:
        e_date = "2016-01-01"
    else:
        e_date = end_date

    urllib3.HTTPConnectionPool
    result =