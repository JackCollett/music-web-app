
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /albums
# With body parameters:
# title=Voyage
# release_year=2022
# artist_id=2
#  Expected response (200 OK):
"""
(No content)
"""
# GET /albums
# Expected response (200 OK):
"""
Album(1, Voyage, 2022, 1)
Album(2, The Cold Nose, 2008, 2)
"""

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
(No content)
"""
def test_post_new_album(web_client):
    response = web_client.post('/submit', data={'title': 'Voyage','release_year': 2022,'artist_id': 2}')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

