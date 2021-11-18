import requests
from bs4 import BeautifulSoup

def web_scraping():
    page = requests.get('https://www.waze.com/en/live-map/directions/tokol-magyarorszag?utm_source=website&utm_medium=homepage&utm_campaign=iframe+module&to=place.ChIJHaMnPRvlQUcR8CYeDCnEAAQ&from=place.ChIJC0BjZOzdQUcR4NUeDCnEAAU')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(Class='wm-routes multiple-routes')
    print(week)







def main():
    web_scraping()



if __name__ == "__main__":
    main()