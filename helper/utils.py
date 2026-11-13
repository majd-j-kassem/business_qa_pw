from enum import Enum
from logging import Logger

from playwright.sync_api import Page

try:
    import allure

    ALLURE_AVAILABLE = True
except ImportError:
    ALLURE_AVAILABLE = False


class LogLevel(Enum):
    """
    LogLevel class: mapping each log type to readable type
    """

    INFO = "info"
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


def log_message(
    logger: Logger, message: str, log_level: LogLevel, attached_to_allure: bool = True
) -> None:
    """
    Log_message: Create a log record based on each record level logging

    Args:
        logger
        message (str): the message to be logged
        log_level (LogLevel): the level of logging of type LogLevel Enum
        attached_to_allure (bool): determines weahter to add the log record to the allure report

    Returns:
        None
    """
    if log_level == LogLevel.INFO:
        logger.info(message)
    elif log_level == LogLevel.DEBUG:
        logger.debug(message)
    elif log_level == LogLevel.WARNING:
        logger.warning(message)
    elif log_level == LogLevel.ERROR:
        logger.error(message)
    elif log_level == LogLevel.CRITICAL:
        logger.critical(message)

    if attached_to_allure and ALLURE_AVAILABLE:
        try:
            allure.attach(
                message,
                name=f"{log_level.value.upper()}",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception:
            logger.exception("Failed to attach log message to Allure")


def take_screenshot(
    page: Page, logger: Logger, name: str = "screenshot"
) -> bytes | None:
    """
    take_screenshot: capture a screenshot of the current page object

    Args:
        page: the current page object
        logger: the logger object
        name (str): the name of the screenshot

    Returns:
        screen_data (bytes) object or None on error
        None : when fails to capture screen
    """
    try:
        screenshot_data = page.screenshot(type="png")
    except Exception:
        logger.exception("Screenshot capture failed")
        return None
    if ALLURE_AVAILABLE:
            try:

                allure.attach(
                    screenshot_data, name=name, attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                logger.exception("Screenshot attachment-allure failed")
    return screenshot_data
    
