import csv
import logging
import os

import yaml
import logs
import scraper

import pandas

config = yaml.safe_load(open("./config.yml", 'rt', encoding='utf8'))


logs.setup_logging(config['logging']['logPath'], os.path.splitext(os.path.basename(__file__))[0])


if __name__ == '__main__':
    logging.info(f"Scraping {config['scraping']['area']} at {config['scraping']['host']}")
    data = scraper.scrape_event_data(f"{config['scraping']['host']}/api/events?area={config['scraping']['area']}"
                                     f"&limit={config['scraping']['limit']}")

    logging.info(f"Saving results to {config['scraping']['exportPath']}")
    keys = data[0].keys()
    with open(config['scraping']['exportPath'], 'w', newline='', encoding="utf8") as f:
        dw = csv.DictWriter(f, keys, delimiter=';')
        dw.writeheader()
        dw.writerows(data)

    logging.info("Scraping finished")
