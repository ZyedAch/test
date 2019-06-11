import logging


# set up logging to file
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
