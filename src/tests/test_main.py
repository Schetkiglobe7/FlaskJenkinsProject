import json

def test_main(app, client):
    res = client.get('/health.json')
    assert res.status_code == 200
    expected = {'status': 'UP'}
    assert expected == json.loads(res.get_data(as_text=True))