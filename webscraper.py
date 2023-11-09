import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get("Paste a Domain here")
soup = BeautifulSoup(page.content, 'html.parser')

all_h1_tags = [element.text for element in soup.select('h1')]
print(all_h1_tags)

# give you all h1 tags 