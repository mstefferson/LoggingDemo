import logging


def foo():
    logger = logging.getLogger(__name__)
    logger.debug('foo')
    logger.info('foo')
    logger.warning('foo')
    logger.error('foo')


class Bar(object):
    def __init__(self, logger=None):
        self.logger = logging.getLogger(__name__)

    def bar(self):
        self.logger.debug('bar')
        self.logger.info('bar')
        self.logger.warning('bar')
        self.logger.error('bar')
