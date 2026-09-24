from app import app


def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Feedback Form' in response.data


def test_submit_feedback():
    client = app.test_client()
    response = client.post('/', data={
        'name': 'Aditya',
        'course': 'Data Science',
        'feedback': 'The course was informative.',
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Aditya' in response.data
    assert b'Data Science' in response.data
