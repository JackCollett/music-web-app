from lib.album import Album

'''
Constructs with an id, title, release_year and artist id
'''
def test_constructs():
    album = Album(1, "Voyage", 2022, 1)
    assert album.id == 1
    assert album.title == "Voyage"
    assert album.artist_id == 1

'''
Albums with equal contents are equal
'''
def test_compares():
    album_1 = Album(1, "Test Title", 1000, 2)
    album_2 = Album(1, "Test Title", 1000, 2)
    assert album_1 == album_2

"""
Albums can be represented as strings
"""
def test_stringifying():
    album = Album(1, "Test Title", 1000, 2)
    assert str(album) == "Album(1, Test Title, 1000, 2)"