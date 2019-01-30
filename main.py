import logging
import lib1
import my_module
import os
import yaml
import logging.config
# import logging.critical


def setup_logging(default_path='logging.yaml',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    my_path = default_path
    value = os.getenv(env_key, None)
    if value:
        my_path = value
    if os.path.exists(my_path):
        with open(my_path, 'rt') as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    logging.info(f"Logger root set in {__name__}")


def main():
    # logger = logging.getLogger()
    setup_logging()
    # send some messages
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')

    # run func1
    lib1.func1()

    # run func1
    my_module.foo()
    bar = my_module.Bar()
    bar.bar()


if __name__ == '__main__':
    main()
