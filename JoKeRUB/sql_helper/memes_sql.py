try:
    from . import BASE, SESSION
except ImportError as e:
    raise Exception("Hello!") from e
from sqlalchemy import Column, String
import re

class AljokerLink(BASE):
    __tablename__ = "aljoker_links"
    key = Column(String(255), primary_key=True)
    url = Column(String(255))

    def __init__(self, key, url):
        self.key = str(key)
        self.url = str(url)


AljokerLink.__table__.create(checkfirst=True)


def get_link(key):
    link = SESSION.query(AljokerLink).get(str(key))
    return link.url if link else None

def add_link(key, url):
    url_match = re.search(r'(https?://\S+)', url)
    if url_match:
        extracted_url = url_match.group(1)
        pattern = r'https://t.me/(?:c/\d+/\d+|[\w_]+)/\d+'
        if re.match(pattern, extracted_url):
            SESSION.add(AljokerLink(key=key, url=extracted_url))
            SESSION.commit()

def delete_link(key):
    link = SESSION.query(AljokerLink).get(str(key))
    if link:
        SESSION.delete(link)
        SESSION.commit()