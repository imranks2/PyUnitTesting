''' About test '''
import json

def test_about(fixture_app, fixture_client):
    ''' about test function '''
    res = fixture_client.get('/about')
    assert res.status_code == 200
    expected = {'About': 'Us'}
    assert expected == json.loads(res.get_data(as_text=True))
