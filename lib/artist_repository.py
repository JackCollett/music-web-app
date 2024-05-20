from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        artists_list = []
        for row in rows:
            artists_list.append(row["artist"])
        return ", ".join(artists_list)
    
    def create(self, artists):
        self._connection.execute(
            "INSERT INTO artists (artist) VALUES (%s)",
            [artists.artist]
        )
        return None