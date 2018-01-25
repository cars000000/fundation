import urllib3
import requests
import bs4
import datetime

http_manager = urllib3.PoolManager()


def get_fundation_value_content(fund_id, start_date=None, end_date=None):
    fund_value_result = {
        "fund_id": fund_id,
        "fund_value_content": ""
    }
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


    try:
        result = requests.get(url=url, params=fields)
    except Exception, e:
        print "error in get_fund_value_content:", fund_id
        print str(e)
        return fund_value_result

    if result.status_code != 200:
        print "failure in get_fund_value_content:", result.url
        return fund_value_result

    if result.text.strip() == "":
        print "blank in get_fund_value_content:", result.url
        return fund_value_result

    fund_value_result["fund_value_content"] = result.text
    return fund_value_result


def get_fund_value(fund_content):
    fund_content["fund_value"] = []

    fund_value_content = fund_content.pop("fund_value_content")
    if fund_value_content == "":
        return fund_content
    #print fund_value_content
    fund_value_content_xml = bs4.BeautifulSoup(fund_value_content, "html.parser")
    #print fund_value_content_xml.children
    table_tag_list = fund_value_content_xml.find_all("table", attrs={"class": "mt1 clear"})
    if len(table_tag_list) != 1:
        return

    for tr in table_tag_list[0].find_all("tr", attrs={"class": ["row1", "row2"]}):
        value_list = [td.text for td in tr.find_all("td")]
        value_date = value_list[0]
        if datetime.datetime.strptime(value_date, "%Y-%m-%d").weekday() in [6,7]:
            continue
        print value_list


        #print tr




def get_fund_id(fund_id=None):
    result = []

    f = open("fund_id_list")
    for line in f.readlines():
        fund_id = line.strip()
        result.append(fund_id)
    f.close()

    if fund_id is None:
        return result
    else:
        if not isinstance(fund_id, str) or not isinstance(fund_id, unicode):
            fund_id = unicode(fund_id)

        if len(fund_id) <= 6:
            fund_id = fund_id.zfill(6)

        if not fund_id.isdigit():
            print "error fund_id. not an integer:", fund_id
            return None

        if len(fund_id) > 6:
            print "error fund_id, too long:", fund_id
            return None


        if fund_id not in result:
            print "error fund_id, doesn't exist:", fund_id
            return None

        return fund_id



if __name__ == '__main__':
    fund_value = get_fundation_value_content("000017")
    fund_value = get_fund_value(fund_value)