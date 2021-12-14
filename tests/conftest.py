#conftest.py
# stores common test fixtures, to share them within the testing directory
# fixtures setup the testing scenarios
# must be placed under /tests folder, and pytest will find them automatically

#================================================================================


import pytest
#import the app object
from urlshort import app as flask_app


# this fixture return the app
@pytest.fixture
def app():
    yield flask_app


# this fixture allows to use an http client to connect to the web site
@pytest.fixture
def client(app):
    return app.test_client()