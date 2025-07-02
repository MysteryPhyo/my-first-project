import argparse
import requests
from bs4 import BeautifulSoup


def get_article_titles(url: str):
    """Return a list of article titles from the page at *url*.

    Titles are extracted from all ``h1`` and ``h2`` elements.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    titles = []
    for tag in soup.find_all(["h1", "h2"]):
        text = tag.get_text(strip=True)
        if text:
            titles.append(text)
    return titles


def main():
    parser = argparse.ArgumentParser(description="Scrape blog article titles.")
    parser.add_argument("url", help="URL of the blog page to scrape")
    args = parser.parse_args()

    titles = get_article_titles(args.url)
    for title in titles:
        print(title)


if __name__ == "__main__":
    main()
