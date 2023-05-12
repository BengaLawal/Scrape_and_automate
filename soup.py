import requests
from bs4 import BeautifulSoup

# Scrape Property24 for price, location and link to listing of a certain area

class Soup:
    def __init__(self):
        self.data = []

    def make_soup(self, property24_url):
        """
        makes up data for self.data - a list of tuples containing price, location and link
        """
        response = requests.get(url=property24_url)
        response.encoding = 'utf-8'
        webpage = response.text

        # getting hold of prices, location and links
        soup = BeautifulSoup(webpage, 'html.parser')
        prices = soup.find_all(name='span', class_='p24_price')
        locations = soup.select(selector='div a span span .p24_location')
        links = soup.select(selector='.js_resultTile a')

        # getting hold of text
        price = [i.getText().strip("R \n\r '' \r\n per day {{price}}") for i in prices]
        location = [i.getText().strip() for i in locations]
        link = [f'https://www.property24.com{i.get("href")}' for i in links]

        # zip the 3 list to make a list of tuples
        # list/tuple is used to view the zipped file in a readable manner
        self.data = list(zip(price, location, link))
        # print(f'length of data: {len(self.data)}')
