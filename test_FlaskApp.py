import pytest
from app import app

@pytest.fixture # fixter helps to start flask app virutally without running it
def client():  # whenever this function get call flask application will start
    return app.test_client()

def test_home(client):
    resp=client.get('/')

    assert resp.status_code==200


