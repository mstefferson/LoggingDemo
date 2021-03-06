import logging
import lib1
import my_module
import util


def inner_fnc():
    logger = logging.getLogger(__name__)
    logger.info('Inner fnc')
    logger.error('Inner fnc')


def main():
    # logger = logging.getLogger()
    util.setup_logging()
    # logger = logging.getLogger(__name__)
    # send some messages
    # logger.debug('debug message')
    # logger.info('info message')
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')

    # inner fnc
    inner_fnc()

    # run func1
    lib1.func1()

    # run func1
    my_module.foo()
    bar = my_module.Bar()
    bar.bar()


if __name__ == '__main__':
    main()
