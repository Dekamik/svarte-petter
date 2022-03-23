import logging
import sys

import requests


def scrape_event_data(url):
    logging.info(f"Scraping {url}")
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Call to {url} returned non-successful response ({response.status_code}). "
                      f"Response: {response.text}")
        sys.exit(1)

    content = response.json()
    data = content['data']
    next_url = content['links']['next_page_url']

    if next_url is not None:
        data.extend(scrape_event_data(next_url))

    return data
