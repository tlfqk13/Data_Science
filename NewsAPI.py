import requests
import json

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f025ff10083546ccb2529360cae91d8e')
response = requests.get(url)
info=response.json()
print(info)
print("*"*80)

#(1) 최신뉴스 건수인 totalResults 를 출력하시오
print(info['totalResults'])
#(2) 최신뉴스별 author를 모두 출력하시오
info_articles=info['articles']
print(type(info_articles))
for i in info_articles :
    author_list=i['author']
    print(author_list)
