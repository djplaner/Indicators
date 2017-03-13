import json

from sqlalchemy.engine.url import URL 
from sqlalchemy import create_engine

def connect():
    CONFIG='/Applications/mappstack-5.6.30-1/apache2/htdocs/moodle/config.json';

    with open(CONFIG) as f:
        conf = json.load(f)

    engine = create_engine(URL(**conf))

    return engine


if __name__ == '__main__':
    connect()
