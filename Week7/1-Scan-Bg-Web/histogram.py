import requests
from bs4 import BeautifulSoup


class Histogram:

    def __init__(self):
        self.__items = {}

    def add(self, item):
        if self.__items.get(item) is None:
            self.__items[item] = 1
        else:
            self.__items[item] += 1

    def count(self, item):
        return self.__items[item]

    def get_dict(self):
        return self.__items

    def make_head_req(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        req = requests.head(url, headers=headers, allow_redirects=True, timeout=2)
        return req.headers["Server"]

    def crawling_sites(self):
        r = requests.get("http://register.start.bg/")
        html_doc = r.text
        soup = BeautifulSoup(html_doc)
        i = 0
        for link in soup.find_all('a'):
            str_link = str(link.get('href'))
            if str_link.startswith("link"):
                try:
                    req_head = self.make_head_req("http://register.start.bg/"+str_link)
                    print(req_head)
                    self.add(req_head)
                    i += 1
                except Exception:
                    pass
            if i == 50:
                break

    def save_in_file(self, file):
        with open(file, 'w') as file_:
            for key, val in self.__items.items():
                file_.write(key + " : " + str(val) + "\n")

    def consolidate_servers(self):
        consolidated = {"nginx": 0, "IIS": 0, "Apache": 0, "lighttpd": 0, "other": 0}
        for key in self.__items.keys():
            for most_common in consolidated.keys():
                if most_common in key:
                    consolidated[most_common] += self.__items[key]
        return consolidated

h = Histogram()
h.crawling_sites()
h.save_in_file("histogram.txt")
print(h.consolidate_servers())
