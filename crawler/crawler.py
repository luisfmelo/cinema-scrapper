import logging

from config import CINEMAS
from crawlers.cinema_factory import cinema_factory
from services.slack_service import notify_slack_message

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Cinema Crawler...\n")

    for cinema in CINEMAS:
        try:
            crawler = cinema_factory(cinema['class'])
            logger.info('Crawling ' + cinema['name'] + '...')

            crawler.get_infinite_scroll_page(cinema['url'])
            crawler.scrap_sessions()
            crawler.close()

        except Exception as e:
            logger.error(str(e))
            import traceback
            notify_slack_message(str(traceback.format_exc()))

        logger.info('Finished crawling ' + cinema['name'] + '.')


main()
