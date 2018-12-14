# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()

import logging


def before_all(context):
    pass


def before_feature(context, feature):
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('api_tests')
    hdlr = logging.FileHandler('./api_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    pass


def before_tag(context, tag):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass
