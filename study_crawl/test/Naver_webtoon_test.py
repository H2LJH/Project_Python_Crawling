import requests
import study_crawl.movie.persistence.MongoDAO as DAO
from bs4 import BeautifulSoup

mDao = DAO.MongoDAO()
page = 1      # 시작 페이지
end_page = 6  # 마지막 페이지
while page < end_page:
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=187351&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('Error URL')
        exit()

    else:
        soup = BeautifulSoup(resp.text, 'html.parser')
        reply_list = soup.select('div.score_result ul li')

        for i, reply in enumerate(reply_list):
            # ======================= 작성자 특정부분 지우기 ======================================
            previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
            cut_index = previous_writer.find('(')

            if cut_index > 0:
                writer = previous_writer.index('(')
            else:
                writer = previous_writer
            # ======================== 시간 지우기 =============================================
            temp_dt  = reply.select('div.score_reple em')[1].text.strip()
            delet_dt = temp_dt.index(' ')
            time_dt  = temp_dt[delet_dt+1:]
            # ==================================================================================
            writer = reply.select('div.score_reple > dl > dt > em')[0].text.strip()[:cut_index]  # 작성자
            score = reply.select('div.star_score > em')[0].text.strip()  # 평점
            review = reply.select('div.score_reple > p > span')[0].text.strip()  # 내용
            # =========================== DB Insert =============================================
            data = {'review': review,
                    'write': writer,
                    'score': score,
                    'reg_dt': time_dt
                    }
            mDao.mongo_insert(data)
            # ===================================================================================
        page += 1
