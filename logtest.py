import logging
from tdlog import logger

logging.basicConfig(level=logging.INFO)
l = logging.getLogger('td_logger.test')
l.addHandler(logger.TreasureDataHandler())

l.info('Some message')
js = { "semicolon" : ";", "at" : "@" }
l.info(js)
