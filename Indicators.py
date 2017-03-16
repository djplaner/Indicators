import json

from sqlalchemy.engine.url import URL 
from sqlalchemy import create_engine

import os
import sys

def connect():

    CONFIG='/Applications/mappstack-5.6.30-1/apache2/htdocs/moodle/config.json';

    with open(CONFIG) as f:
        conf = json.load(f)

    engine = create_engine(URL(**conf))

    return engine


def config():
    CONFIG='/Applications/mappstack-5.6.30-1/apache2/htdocs/moodle/lms.json';

    with open(CONFIG) as f:
        conf = json.load(f)

    return conf


if __name__ == '__main__':
    connect()
