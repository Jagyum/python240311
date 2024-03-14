import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        blog_list = soup.find_all('li', class_='bx')
        
        for blog in blog_list:
            blog_title = blog.find('a', class_='api_txt_lines total_tit').text
            blog_url = blog.find('a', class_='api_txt_lines total_tit')['href']
            blog_date = blog.find('span', class_='sub_time sub_txt').text
            
            print("블로그명:", search_keyword)
            print("글 제목:", blog_title)
            print("URL:", blog_url)
            print("날짜:", blog_date)
            print("\n")
    else:
        print("Error:", response.status_code)

# 검색 키워드
search_keyword = "맥북에어"
crawl_naver_blog(search_keyword)
