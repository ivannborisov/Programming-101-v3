class Song:

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def __str__(self):
        return "{artist} - {name} from {album} - {length}".format(self.__name, self.__artist, self.__album, self.__length)

    def __repr__(self):
        return self.__title

    def __hash__(self):
        return hash(self.__title + self.__artist)

    def __eq__(self, other):
        if self.__title == other.__title and self.__artist == other.__artist:
            return True
        else:
            return False

    def getArtist(self):
        return self.__artist

    def length(self, seconds=False):

        if seconds:
            length_list = self.__length.split(':')
            minutes = int(length_list[0])
            seconds = int(length_list[1])

            length_in_sec = minutes*60 + seconds
            return length_in_sec
        else:
            return self.__length
