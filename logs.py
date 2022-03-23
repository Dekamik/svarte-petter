import os.path
from datetime import datetime
import logging


def setup_logging(log_path, name):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    logging.basicConfig(
        filename=f"{log_path}/{name}_{datetime.utcnow().isoformat().replace(':', '')}.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]  %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s: %(levelname)s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
