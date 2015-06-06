import requests


class GitGraph:
    def __init__(self):
        self.followers = []
# (username , level)
        self.following = []

    def build_network():
        pass


class DirectedGraph:

    def __init__(self):
        self.graph = {}
        self.c_id = '2b8872e3016e2f370ef7'
        self.c_sec = 'dea707f9a0a29e03b65262fd5d99e0f1a98a2554'
        self.git_auth = '?client_id={}&client_secret={}'.format(self.c_id,self.c_sec)
        self.depth = 4

    def add_edge(self, node_a, node_b):
        if node_a in self.graph.keys():
            self.graph[node_a].add(node_b)
        else:
            self.graph[node_a] = set()
            self.graph[node_a].add(node_b)

    def get_neighbors_for(self, node):
        url = 'https://api.github.com/users/{}{}'.format(node, self.git_auth)
        r = requests.get(url)
        r_json = r.json()
        followers_url = r_json['followers_url']
        foll_req = requests.get(followers_url + self.git_auth)
        followers = [x['login'] for x in foll_req.json()]
        return followers

    def build_network(start, level):
        pass


graph = DirectedGraph()
# graph.get_neighbors_for('radorado')
graph.add_edge('ivan', 'pesho')
graph.add_edge('ivan', 'pesho')
graph.add_edge('ivan', 'dako')
graph.add_edge('pesho', 'dako')
print(graph.graph)

"""
 def build_networpk(start, level):
    v = set()
    q = []
    v = add(start)
    q.append((0,start))
    while len(q) != 0:
        cl , ch = q.pop(0)          //cl- current level cn- current name
        if cl > level:
            break
        network = get_network_for(cn)

        for follower in network['followers']
            if follower not in v:
                    g.add_edge(followers)
                    v.add(follower)
                    q.append((cl+1, follower))

            g.add_edge(cn,following)
"""
"""
    graph = {
        ''
    }
"""
