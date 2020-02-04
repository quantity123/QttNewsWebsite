import logging
from QttNewsWebsite.settings import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('django.request')

def testLog(request):
    logger.warning('warning log')