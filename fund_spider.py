import urllib3

http_manager = urllib3.PoolManager()

def get_fundation_history(fund_id, start_date=None, end_date=None):
    url_prefix = "http://www.dayfund.cn/fundvalue/"
    url = url_prefix + fund_id + ".html"

    if start_date is None:
        s_date = "2016-01-01"
    else:
        s_date = start_date

    if end_date is None:
        e_date = "2018-01-01"
    else:
        e_date = end_date

    fields = {
        "sdate": s_date,
        "edate": e_date,
    }

    result = http_manager.request(method="GET", url=url, fields=fields)
    print result.data

if __name__ == '__main__':
    get_fundation_history("5035")