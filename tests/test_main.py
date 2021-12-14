# main tests file
from urlshort import app




#test the index page

def test_index_status_code(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_shorten_in_index(client):
    resp = client.get('/')
    assert b"shorten" in resp.data.lower()