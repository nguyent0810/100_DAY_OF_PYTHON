from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,'html.parser')
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
     text = article_tag.getText()
     article_texts.append(text)
     link = article_tag.get("href")
     article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)
index_max = max(range(len(article_upvotes)), key=article_upvotes.__getitem__)
print(f"The highest article score is {article_texts[index_max]} with score {article_upvotes[index_max]} Refer: {article_links[index_max]}")
