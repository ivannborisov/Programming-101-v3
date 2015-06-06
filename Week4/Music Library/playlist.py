from Song import Song


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.__playlist = []

    def playlist(self):
        return self.__playlist

    def add_song(self, song):
        self.__playlist.append(song)

    def remove_song(self, song):
        try:
            self.__playlist.remove(song)
        except ValueError as e:
            pass

    def add_songs(self, songs):
        self.__playlist += songs

    def total_length(self):
        total_in_sec = sum([x.length(seconds=True) for x in self.playlist()])
        total_min = total_in_sec // 60
        total_sec = total_in_sec % 60
        return "{}:{}".format(total_min, total_sec)

    def artist(self):
        artist_list = [x.getArtist() for x in self.playlist()]
        art_song_dict = {x.getArtist(): artist_list.count(x.getArtist()) for x in self.playlist()}
        artist_str = ''
        for key, elem in art_song_dict.items():
            artist_str += key
            artist_str += ':'
            artist_str += str(elem)
            artist_str += '\n'
        return artist_str

    def next_song(self):
        pass


newsong = Song("Python-a", "Konstantin", "Obadi mi se", "3:10")
newsong2 = Song("Python-a2", "Konstantin2", "Obadi mi se", "3:10")
newsong3 = Song("Python-a3", "Konstantin2", "Obadi mi se", "3:10")
newsong4 = Song("Python-a4", "Konstantin3", "Obadi mi se", "3:10")
newplaylist = Playlist("Retro chalga 2015")

songs = [newsong2, newsong3, newsong4]

newplaylist.add_song(newsong)
newplaylist.add_songs(songs)
print(newplaylist.artist())

try:
    while true:
        pass
except Exception as e:
    print(e)
