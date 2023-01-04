# pylint: disable=redefined-outer-name
''' Config test'''
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    ''' app '''
    yield flask_app


@pytest.fixture
def client(app):
    ''' client'''
    return app.test_client()
