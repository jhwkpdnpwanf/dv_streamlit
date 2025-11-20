import os
import sys
sys.path.append('./data')
import my_apikeys as mykeys
import urllib.request
import pandas as pd
import json


client_id = mykeys.naver_client_id
client_secret = mykeys.naver_client_secret

# 파라미터 설정
# display_count : 한 페이지에 표시할 검색 결과 수
# num_data : 검색할 데이터 개수
# sort : 날짜순 (date) or 유사도순 (sim)
display_count = 100
num_data = 1000
#sort = 'sim'
sort = 'date'

encText = urllib.parse.quote("서울시 부동산")

# 결과를 저장할 list
results = []

# 검색 결과 요청
for idx in range(1, num_data+1, display_count):

    # 요청 URL
    url = "https://openapi.naver.com/v1/search/news?query=" + encText \
        + f"&start={idx}&display={display_count}&sort={sort}"

    # 요청 객체
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 응답
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        # 응답 본문
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        results = results + response_dict['items']
    else:
        print("Error Code:" + rescode)

# 데이터 개수
print(f'총 데이터 개수: {len(results)}')



# -----------------------------
# csv로 저장
# -----------------------------

from datetime import datetime
import re

df = pd.DataFrame()

# HTML 태그 제거
remove_tags = re.compile(r'<.*?>')

for item in results:
    new_data = pd.DataFrame(
        data={
            # 날짜는 datetime 객체로 변환
            'pubDate': datetime.strptime(item['pubDate'], "%a, %d %b %Y %H:%M:%S +0900"),

            # title, description에서 HTML 태그 제거
            'title': re.sub(remove_tags, '', item['title']),
            'description': re.sub(remove_tags, '', item['description'])
        },
        index=[0]
    )

    df = pd.concat([df, new_data], ignore_index=True)

# 확인용
df.head()
df.info()

df.to_csv('./data/naver_news.csv', encoding='utf-8')