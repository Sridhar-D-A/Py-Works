import logging

formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')


def setup_logger(name, log_file, level):
    # you can set up as many logger as you want

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# first file logger
logger = setup_logger('first_logger', 'first_logfile.log', 'INFO')
logger.info('This is just info message')

# second file logger
super_logger = setup_logger('second_logger', 'second_logfile.log', 'DEBUG')
super_logger.error('This is an error message')


def testing_logger():
    logger.info("this is first log file")
    super_logger.info("this is second log file")
    a = 20
    b = 30
    c = a * b
    d = 1
    for i in range(1, 5):
        d = d * i
        super_logger.info(i)
        logger.info(i)

    logger.info('{} is one result and {} is another result'.format(c, d))
    logger.warning('{} is one result and {} is another result'.format(c, d))
    super_logger.info('{} is one result and {} is another result'.format(c, d))
    super_logger.debug('{} is one result and {} is another result'.format(c, d))

testing_logger()
