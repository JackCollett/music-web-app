class Artist:
    def __init__(self, artist):
        #self.id = id
        self.artist = artist
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{self.artist}"