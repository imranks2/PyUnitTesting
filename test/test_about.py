import json


def test_about(app, client):
    res = client.get('/about')
    assert res.status_code == 200
    expected = {'About': 'Us'}
    assert expected == json.loads(res.get_data(as_text=True))
