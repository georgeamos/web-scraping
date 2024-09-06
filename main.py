import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.text
    else:
        return None


if __name__ == "__main__":
    url = "https://www.linkedin.com/"
    title = fetch_data(url)
    if title:
        print(f"Title of the page: {title}")
    else:
        print(f"Failed to retrieve data.")
