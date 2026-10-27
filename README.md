# BeautifulSoup Quote Scraper

## Overview
A Python web scraping project that fetches a public webpage, extracts quotes and author names using BeautifulSoup, and saves the cleaned information as JSON.

## Features
- Sends HTTP requests using `requests`.
- Handles network errors, timeouts, and HTTP error responses.
- Parses HTML using BeautifulSoup.
- Extracts quotes, authors, and tags using CSS selectors.
- Checks for missing HTML elements.
- Saves structured data to `quotes.json`.

## Technologies
- Python 3
- Requests
- BeautifulSoup4
- JSON

## Source Website
https://quotes.toscrape.com/

I selected Quotes to Scrape because it is a public practice website intended for learning web scraping. The project collects only quote text, author names displayed with those quotes, and associated tags. It does not access login-protected pages or collect private personal data.

Before running a scraper, check the website's terms, robots.txt, and applicable rules. Public accessibility alone does not guarantee permission for every type of scraping or reuse.

## Installation
Install the dependencies:

`python -m pip install -r requirements.txt`

## Run
Execute:

`python scraper.py`

The program fetches the webpage and writes extracted records to `quotes.json`.

## Output Format
Each JSON record contains:
- `quote`: extracted quote text
- `author`: displayed author name
- `tags`: associated tags

## Error Handling
The program handles request failures and skips records when quote or author elements are missing.

## Future Improvements
- Extract quotes across multiple pages.
- Add command-line options for the output filename.
- Save results as CSV or plain text.
- Add automated tests for HTML selectors.
