from urllib.parse import urlparse
from typing import List, Tuple, Any

DICTIONARY = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def get_sources(soup: object, url: Any) -> List[Tuple[Any, Any, str]]:
    links = []
    find_all = soup.find_all(DICTIONARY.keys())
    for tag in find_all:
        atr = DICTIONARY.get(tag.name)
        file_link = tag.get(atr)
        if is_same_domain(url, file_link):
            links.append((file_link, tag, atr))
    return links


def is_same_domain(url, link):
    if not link:
        return False
    link_netloc = urlparse(link).netloc
    url_netloc = urlparse(url).netloc
    return link_netloc == url_netloc or not link_netloc
