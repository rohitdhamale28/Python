import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "MyWikipediaBot/1.0 (contact@example.com) Python-requests"
}

url = "http://quotes.toscrape.com/"
response = requests.get(url,headers=headers)

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")


soup = BeautifulSoup(html_content, "html.parser")

quotes = soup.find_all("div", class_="quote")
print(f"Total quotes found: {len(quotes)}")

print(quotes[0])

quotes_css = soup.select("div.quote")
