import requests
from bs4 import BeautifulSoup
import sqlite3

db = sqlite3.connect('domains.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


class CrawlingStartBG:

    DEPTH = 4

    def __init__(self):
        self.__items = {}

    def empty_table(self, table_name):
            cursor.execute("DELETE FROM {}".format(table_name))
            db.commit()

    def make_head_req(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        req = requests.head(url, headers=headers, allow_redirects=True, timeout=2)
        return req

    def save_domain(self, domain, start_href):
        query = "INSERT INTO domains(name,start_href) VALUES ('{}','{}')".format(domain,start_href)
        cursor.execute(query)
        db.commit()

    def has_domain(self, domain, table_name):
        last_char = domain[-1:]
        if last_char == '/':
            domain = domain[:-1]
        query = "SELECT name FROM {} WHERE name = '{}' LIMIT 1".format(table_name,domain)
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        return True

    def save_startbg_domain(self, domain):
        last_char = domain[-1:]
        if last_char == '/':
            domain = domain[:-1]
        query = "INSERT INTO startbg_visited_domains(name) VALUES ('{}')".format(domain)
        cursor.execute(query)
        db.commit()

    def get_only_domain(self, domain):
        dom_split = domain.split('/')
        return dom_split[2]

    def crawling_site(self, site, depth=1):
        r = requests.get(site)
        html_doc = r.text
        soup = BeautifulSoup(html_doc)
        if self.has_domain(site, 'startbg_visited_domains') is False:
            self.save_startbg_domain(site)

        for link in soup.find_all('a'):
            str_link = str(link.get('href'))

            if ".start." in str_link and "www.start.bg" not in str_link:
                if self.has_domain(str_link, 'startbg_visited_domains') is False or CrawlingStartBG.DEPTH == 1:
                    if depth <= CrawlingStartBG.DEPTH:
                        print("Crawling site:"+str_link)
                        self.crawling_site(str_link, depth+1)

            elif str_link.startswith("link.php?id"):
                try:
                    req_head = self.make_head_req("http://start.bg/"+str_link)
                    domain = self.get_only_domain(req_head.url)
                    if ".start." not in domain and self.has_domain(domain, 'domains') is False:
                        print("Domain:"+str_link)
                        self.save_domain(domain, str_link)
                except Exception:
                    print("Fail request")

    def make_real_domain(self, domain):
        if "www." not in domain:
            new_dom = "www." + domain
        return "http://" + new_dom

    def take_domain_server(self, domain):
        domain = self.make_real_domain(domain)
        try:
            req = self.make_head_req(domain)
            return req.headers["Server"]
        except Exception:
            return "Fail"

    def take_all_domains(self):
        result = cursor.execute("SELECT name FROM domains")
        return result

    def update_domain_server(self, domain, server):
        query = "UPDATE domains SET server='{}' WHERE name = '{}'".format(server, domain)
        cursor.execute(query)
        db.commit()

    def update_all_domains(self):
        domains = self.take_all_domains()
        domains = domains.fetchall()
        for dom in domains:
            server = self.take_domain_server(dom['name'])
            if server is not False:
                self.update_domain_server(dom['name'], server)
            print(dom['name'] + " " + server)


craw = CrawlingStartBG()

craw.crawling_site("http://start.bg/")

db.close()
