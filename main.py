import random
import time

from splinter import Browser


url = 'http://dle.rae.es/srv/random'


with Browser('firefox') as browser:
    while True:
        browser.visit(url)
        with open('rae_crawl.txt', 'a') as output:
            output.write(browser.html + '\n')

        time.sleep(random.randint(45, 75))
