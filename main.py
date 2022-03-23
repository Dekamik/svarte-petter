import logging
import os

import yaml
import logs

config = yaml.safe_load(open("./config.yml"))


logs.setup_logging(config['logging']['logPath'], os.path.splitext(os.path.basename(__file__))[0])


if __name__ == '__main__':
    logging.info(f"Scraping {config['scraping']['area']} at {config['api']['host']}")
