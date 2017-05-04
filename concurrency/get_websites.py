import concurrent.futures as futures
import requests
from bs4 import BeautifulSoup

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url):
    """ Retrieve a single page and report the URL and contents """

    r = requests.get(url)
    return r.text

# We can use a with statement to ensure threads are cleaned up promptly
with futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url): url for url in URLS}
    for future in futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            webpage = BeautifulSoup(data, "html.parser")
            links = webpage.find_all('a')
            print("Links in {0}: {1}".format(webpage.title.string, len(links)))