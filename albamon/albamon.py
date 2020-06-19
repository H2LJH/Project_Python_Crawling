import requests
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

cnt = 0
page = 1
timer = time.time()
while True:
    url = 'http://www.albamon.com/list/gi/mon_gi_tot_list.asp?page={}&scd='.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('URL Error')
    else:
        html = urlopen(url).read().decode('cp949', 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        alba_list = soup.select('div.gListWrap tbody tr')
        list_temp = []
# 알바 리스트 ===============================================================================================
    for work_list in alba_list:
        area       = work_list.select('td.area')[0].text.strip()[3:].lstrip('\n')
        main_title = work_list.select('p.cName')[0].text.strip()
        sub_title  = work_list.select('p.cTit')[0].text.strip()
        work_cat   = work_list.select('p.money')[0].find('img')['alt']
        work_pay  = work_list.select('p.won')[0].text.strip()
        work_addr = 'http://www.albamon.com/' + work_list.select('p.cName')[0].find('a')['href']
        list_temp  = [area,     main_title, sub_title,
                      work_cat, work_pay,   work_addr]
        cnt += 1
        print('지역 :', area)
        print('제목 :', main_title)
        print('설명 :', sub_title)
        print('상세 :', work_addr, '\n===================================================================\n')
    # ======================================================================================================
    print('총 구인 등록수 :', cnt)
    print('총 검색 페이지 :', page)
    if not list_temp:
        end_time = time.time() - timer
        print(end_time)
        break
    page += 1