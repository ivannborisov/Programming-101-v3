import json
from Panda import Panda


class PandaNetwork:

    def __init__(self):
        self.__network = {}

    def take_network(self):
        return self.__network

    def has_panda(self, panda):
        if panda in self.__network:
            return True
        return False

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception('Padata e vutre')

        self.__network[panda] = []

    def are_friends(self, panda1, panda2):
        if panda1 in self.__network[panda2] and panda2 in self.__network[panda1]:
            return True
        else:
            return False

    def make_fiends(self, panda1, panda2):

        if self.are_friends(panda1, panda2):
            raise Exception('Pandas already friends')

        self.__network[panda1].append(panda2)
        self.__network[panda2].append(panda1)

    def friends_of(self, panda):
        if panda not in self.__network:
            return False

        return self.__network[panda]

    def connection_level(self, start_panda, end_panda):
        visited_pandas = set()

        queue = []

        path_to = {}

        queue.append(start_panda)
        visited_pandas.add(start_panda)
        path_to[start_panda] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_panda = queue.pop(0)
            if current_panda is end_panda:
                found = True
                break

            for neighbour in self.__network[current_panda]:
                if neighbour not in visited_pandas:
                    path_to[neighbour] = current_panda
                    visited_pandas.add(neighbour)
                    queue.append(neighbour)
        path_length = 0
        if found:
            while path_to[end_panda] is not None:
                path_length += 1
                end_panda = path_to[end_panda]

        return path_length

    def net_to_json(self):
        save_net = {}

        for panda in self.__network:
            friends = [repr(panda_friend) for panda_friend in self.__network[panda]]
            save_net[repr(panda)] = friends

        return json.dumps(save_net, indent=True)

    def save_network(self):
        with open('network.json', "w") as f:
                f.write(self.net_to_json())

    def load(self):
        with open('network.json', "r") as f:
            contents = f.read()
            json_network = json.loads(contents)

            for panda in json_network:
                for friends in json_network[panda]:

                    p1 = eval(panda)
                    p2 = eval(friends)
                    if not self.are_friends(p1, p2):
                        self.make_friends(p1, p2)
