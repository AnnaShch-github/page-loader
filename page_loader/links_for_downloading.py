from urllib.parse import urlparse

from bs4 import BeautifulSoup

DICTIONARY= {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}

def links_for_dowloads(soup, url):
    list_of_links = []
    for key in DICTIONARY.keys():
        find_all = soup.find_all(key)
        atr = DICTIONARY.get(key)
        for link_to_download in find_all:
            file_link = link_to_download.get(atr)
            if same_domain(url, file_link):
                list_of_links.append((file_link, link_to_download, atr))
            else:
                continue
    return list_of_links

def same_domain(url, link):
    if not link:
        return False
    link_netloc = urlparse(link).netloc
    url_neloc = urlparse(url).netloc
    if link_netloc == url_neloc or not link_netloc:
        return True
    else:
        return False
