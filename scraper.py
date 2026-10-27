
import json
import time
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
HEADERS = {
    "User-Agent": "LearningQuoteScraper/1.0 (educational project)"
}
MAX_QUOTES = 20
TIMEOUT = 10


def fetch_page(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.text

    except requests.RequestException as error:
        print("Unable to fetch webpage:", error)
        return None


def extract_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    # Keep selectors together so they are easy to update.
    quote_selector = "div.quote"
    text_selector = "span.text"
    author_selector = "small.author"
    tag_selector = "div.tags a.tag"

    for item in soup.select(quote_selector):
        quote_element = item.select_one(text_selector)
        author_element = item.select_one(author_selector)

        # Skip incomplete records safely.
        if quote_element is None or author_element is None:
            continue

        quote_text = quote_element.get_text(" ", strip=True)
        author = author_element.get_text(" ", strip=True)
        tags = [
            tag.get_text(" ", strip=True)
            for tag in item.select(tag_selector)
        ]

        results.append({
            "quote": quote_text,
            "author": author,
            "tags": tags
        })

        if len(results) >= MAX_QUOTES:
            break

    return results


def save_json(data, filename="quotes.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    print("Fetching public quotes webpage...")

    html = fetch_page(URL)
    if html is None:
        return

    quotes = extract_quotes(html)

    if not quotes:
        print("No quotes found. The webpage structure may have changed.")
        return

    save_json(quotes)
    print(f"Saved {len(quotes)} quotes to quotes.json")

    # Be polite if you later extend this to multiple requests.
    time.sleep(1)

    print("\nFirst few records:")
    for item in quotes[:3]:
        print(f"\nQuote: {item['quote']}")
        print(f"Author: {item['author']}")
        print(f"Tags: {', '.join(item['tags'])}")


if __name__ == "__main__":
    main()
