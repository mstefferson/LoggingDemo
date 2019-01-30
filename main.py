import logging
import lib1
import my_module
import os
import yaml
import logging.config
# import logging.critical

print('simple_example')
print(__name__)


def setup_logging(default_path='logging.yaml',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    my_path = default_path
    print('my_path', my_path)
    value = os.getenv(env_key, None)
    if value:
        my_path = value
        print(my_path)
    if os.path.exists(my_path):
        with open(my_path, 'rt') as f:
            config = yaml.safe_load(f)
        print(config)
        logging.config.dictConfig(config)
        print(logging.getLogger())
    else:
        logging.basicConfig(level=default_level)


def main():
    # logger = logging.getLogger()
    setup_logging()
    # logger = logging.getLogger(__name__)
    # create logger
    # logger = logging.getLogger('simple_example')
    # 'application' code
    logging.debug('debug message')
    logging.info('info message')
    logging.warn('warn message')
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
