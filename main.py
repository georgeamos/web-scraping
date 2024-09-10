import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        description = soup.find('meta', {'name': 'description'})
        description_content = description['content'] if description else 'No description available'
        return title, description_content
    else:
        return None, None


if __name__ == "__main__":
    url = "https://www.oracle.com/"
    page_title, page_description = fetch_data(url)
    if page_title:
        print(f"Title of the page: {page_title}")
        print(f"Description: {page_description}")
    else:
        print(f"Failed to retrieve data.")
