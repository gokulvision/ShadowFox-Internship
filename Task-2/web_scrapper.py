# Q1: Web scraper using requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title:
        print("Page Title:", soup.title.text)
    
    headings = soup.find_all(["h1", "h2"])

    print("\nHeadings:")
    for heading in headings:
        print(heading.text.strip())
else:
    print("Failed to fetch webpage")
