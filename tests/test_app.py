# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Voyage, 2022, 1)"

"""
Album(1, Voyage, 2022, 1)
Album(2, The Cold Nose, 2008, 2)
"""
def test_post_new_album(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums', data = {'title': 'The Cold Nose','release_year': '2008','artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Album(1, Voyage, 2022, 1)\nAlbum(2, The Cold Nose, 2008, 2)"

"""
Test with no data
"""
def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == '' \
        "You need to submit a title, release_year, and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Album(1, Voyage, 2022, 1)"

"""
When I call GET /artists
I get a list of all the current artists
"""
def test_get_all_artists(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When i call POST /artists with a new artist
Then I add a new artist and then when i call GET i can see it added
"""
def test_post_new_artist(db_connection, web_client):
    db_connection.seed("seeds/artists_table.sql")
    response = web_client.post('/artists', data = {'artist': 'Beyonce'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Beyonce"

# === End Example Code ===