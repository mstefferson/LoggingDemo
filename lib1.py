import logging

print('lib1')
print(__name__)


def func1():
    logger = logging.getLogger(__name__)
    # print(__name__)
    # print('Printing in func1')
    logger.debug('In fnc1')
    logger.info('In fnc1')
    logger.warning('In fnc1')
    logger.error('In fnc1')
