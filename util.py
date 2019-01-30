import yaml
import logging.config
import os


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
    logging.info(f"Logger initialized in {__name__}")
