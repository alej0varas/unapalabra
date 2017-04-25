import random

from splinter import Browser
from selenium.common.exceptions import TimeoutException, WebDriverException


PROXIES_FILENAME = 'proxies.txt'
url = 'http://dle.rae.es/srv/random'


def get_proxy_string():
    proxies = open(PROXIES_FILENAME, 'r').readlines()
    proxy_string = random.choice(proxies)
    return proxy_string


def get_proxy(proxy_string):
    proxy = [
        '--proxy=' + proxy_string.strip(),
        '--proxy-type=http',
    ]
    return proxy


def remove_proxy(proxy):
    proxies = open(PROXIES_FILENAME, 'r').readlines()
    proxies.remove(proxy)
    with open(PROXIES_FILENAME, 'w') as proxies_file:
        proxies_file.writelines(proxies)
    print('remove:', proxy)


while True:
    proxy_string = get_proxy_string()
    proxy = get_proxy(proxy_string)
    try:
        with Browser('phantomjs', service_args=proxy) as browser:
            try:
                browser.visit(url)
                if not 'Real Academia Española' in browser.html:
                    remove_proxy(proxy_string)
                else:
                    with open('rae_crawl.txt', 'a') as output:
                        output.write(browser.html + '\n')
            except (TimeoutException, WebDriverException) as e:
                remove_proxy(proxy_string)
    except OSError:
        pass
