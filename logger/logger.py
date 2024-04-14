import sys
import logging


def setup_logger():
    logger = logging.getLogger('logger')
    stdout = logging.StreamHandler(stream=sys.stdout)

    formatter = logging.Formatter(
        "%(name)s: %(asctime)s | [%(levelname)s] | %(filename)s:%(lineno)s %(message)s"
    )

    stdout.setFormatter(formatter)
    logger.addHandler(stdout)

    logger.setLevel(level=logging.INFO)
