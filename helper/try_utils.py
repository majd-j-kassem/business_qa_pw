import logging
from utils import LogLevel, log_message

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("demo")


log_message(logger, "Test message", LogLevel.CRITICAL, False)