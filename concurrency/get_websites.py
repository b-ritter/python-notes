import concurrent.futures as futures
import requests
from bs4 import BeautifulSoup

def load_url(url):
    """ Retrieve a single page and report the URL and contents """
    req = requests.get(url)
    return req.get('text')

def get_number_of_links(urllist):
    """ Get a list of webpages and count the number of links in it """
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        FUTURE_TO_URL = {executor.submit(load_url, url): url for url in urllist}
        for future in futures.as_completed(FUTURE_TO_URL):
            url = FUTURE_TO_URL[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                webpage = BeautifulSoup(data, "html.parser")
                links = webpage.find_all('a')
                yield {
                    "url": url,
                    "page_title": webpage.title.string,
                    "num_links": len(links)
                    }

if __name__ == "__main__":
    URLS = ['http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'http://some-made-up-domain.com/']

    LINKS = get_number_of_links(URLS)
    print(list(LINKS))
