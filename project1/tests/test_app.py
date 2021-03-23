import sys
sys.path.append('/Users/dmitry/Desktop/summary-tasks/project1/app')
from app import client


def test_put():
    input_data = [
        {
            'id': 0,
            'lesson': [0, 1],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        {
            'id': 1,
            'lesson': [0, 1000],
            'pupil': [100, 200, 400, 650, 780, 920],
            'tutor': [150, 250, 600, 900]
        },
        {
            'id': 2,
            'lesson': [0, 1000],
            'pupil': [100, 200, 400, 650, 780, 920],
            # Skip 'tutor' parameter
        }
    ]

    res = client.post('/api', json=input_data)

    assert res.status_code == 200
    assert len(res.get_json()) == 3
    assert res.json[0]["second"] == "0"
    assert res.json[0]["error_message"] == "Success"
    assert res.json[1]["second"] == "223"
    assert res.json[2]["error_message"] == "Wrong format data"
