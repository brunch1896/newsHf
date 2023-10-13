from bs4 import BeautifulSoup
import requests
import clipboard
import streamlit as st


header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}
url = st.text_input('news url', ' ')
text = str(requests.get(url, headers=header).text)

soup = BeautifulSoup(text, 'html.parser')

# h1 = soup.find('h1', class_='post_title').text.strip()
h1 = soup.find('h1').get_text()

# 找到正文内容所在的标签
content_tag = soup.find("div", class_="post_body")

# 提取正文内容
# content = content_tag.get_text("\n")
content = content_tag.get_text()
content = content[:2200]




API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with st.container():
   st.write(query(content))