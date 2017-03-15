import json

from sqlalchemy.engine.url import URL 
from sqlalchemy import create_engine

def connect():
    CONFIG='../config.json';

    with open(CONFIG) as f:
        conf = json.load(f)

    engine = create_engine(URL(**conf))

    return engine


def config():
    CONFIG='../lms.json';

    with open(CONFIG) as f:
        conf = json.load(f)

    return conf


if __name__ == '__main__':
    connect()
