import requests
from bs4 import BeautifulSoup
import unicodedata


cookies = {
    'UqFBpCf3nDqWUw__': 'v1AuwFgw__IYG',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'UqFBpCf3nDqWUw__=v1AuwFgw__IYG',
    'Origin': 'https://usfweb.usf.edu',
    'Referer': 'https://usfweb.usf.edu/DSS/StaffScheduleSearch/StaffSearch/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'P_SEMESTER': '202301',
    'P_SESSION': '',
    'P_CAMPUS': 'T',
    'P_COL': '',
    'P_DEPT': '',
    'p_status': '',
    'p_ssts_code': '',
    'P_CRSE_LEVL': '',
    'P_REF': '',
    'P_SUBJ': '',
    'P_NUM': '',
    'P_TITLE': '',
    'P_CR': '',
    'p_insm_x_inad': 'YAD',
    'p_insm_x_incl': 'YCL',
    'p_insm_x_inhb': 'YHB',
    'p_insm_x_inpd': 'YPD',
    'p_insm_x_innl': 'YNULL',
    'p_insm_x_inot': 'YOT',
    'p_day_x': 'no_val',
    'p_day': 'no_val',
    'P_TIME1': '',
    'P_INSTRUCTOR': '',
    'P_UGR': '',
}

response = requests.post('https://usfweb.usf.edu/DSS/StaffScheduleSearch/StaffSearch/Results', cookies=cookies, headers=headers, data=data)
parsedData =  BeautifulSoup(response.text, 'html.parser')

courseTable = parsedData.find("table", {"id": "results"})
coursesRows = courseTable.find_all('tr')
coursesRows.pop(0)

courseInfoArray = []

for row in coursesRows:
    courseFields = row.find_all('td')
    try:
        courseCRN = unicodedata.normalize("NFKD",courseFields[3].text)
        courseCRS = unicodedata.normalize("NFKD",courseFields[4].text)
        courseDict = {'courseCRN': courseCRN, 'courseCRS': courseCRS}
        courseInfoArray.append(courseDict)
    except:
        pass

print(courseInfoArray)
    