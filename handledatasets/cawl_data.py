import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}


def get_page_data(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    comments = soup.find_all('div', itemprop='text')

    comment_texts = []
    for comment in comments:
        if not comment.find_parent('blockquote'):
            text = ' '.join(comment.stripped_strings)
            if not re.search(r'\bsaid\b', text) and str.__len__(text) <= 250:
                comment_texts.append(text)
    return comment_texts


base_url = "https://voz.vn/t/nhap-ngu-thi-xac-dinh-mat-nguoi-yeu.154776"


def get_data_from_multiple_pages(base_url, num_pages):
    all_comments = []
    for page_num in range(1, num_pages + 1):
        url = f"{base_url}/page-{page_num}"
        comments_on_page = get_page_data(url)
        all_comments.extend(comments_on_page)
    return all_comments


# Số trang bạn muốn lấy dữ liệu
num_pages = 16
comments = get_data_from_multiple_pages(base_url, num_pages)

# Tạo DataFrame từ danh sách bình luận với cột "Sentence"
df_comment = pd.DataFrame(comments, columns=["Sentence"])

# Chèn cột "Emotion" vào vị trí 0 (đầu tiên) của DataFrame
df_comment.insert(0, "Emotion", "")

# Lưu DataFrame vào một tệp Excel
excel_file = "comments_data.xlsx"
df_comment.to_excel(excel_file, index=False)

print(f"Dữ liệu đã được lưu vào tệp Excel: {excel_file}")