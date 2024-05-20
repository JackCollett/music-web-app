from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call #all
I get all the artists in the artists table
"""
def test_all(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == "Pixies, ABBA, Taylor Swift, Nina Simone"