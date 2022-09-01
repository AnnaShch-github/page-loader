import logging
import sys

logger = logging.getLogger('logger')
logger_error = logging.getLogger('logger_error')

logger.setLevel(logging.DEBUG)
logger_error.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter_error = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler(stream=sys.stdout)
handler_error = logging.StreamHandler(stream=sys.stderr)

handler.setLevel(logging.DEBUG)
handler_error.setLevel(logging.ERROR)

handler.setFormatter(formatter)
handler_error.setFormatter((formatter_error))

logger.addHandler(handler)
logger_error.addHandler(handler_error)
