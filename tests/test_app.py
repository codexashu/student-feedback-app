from app import app, feedback_list


def setup_function():
    feedback_list.clear()


def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Feedback Form' in response.data


def test_submit_feedback_with_valid_niet_email():
    client = app.test_client()
    response = client.post('/', data={
        'name': 'Aditya',
        'email': 'student@niet.co.in',
        'course': 'Data Science',
        'feedback': 'The course was informative.',
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Aditya' in response.data
    assert b'student@niet.co.in' in response.data


def test_reject_non_niet_email():
    client = app.test_client()
    response = client.post('/', data={
        'name': 'Aditya',
        'email': 'student@gmail.com',
        'course': 'Data Science',
        'feedback': 'The course was informative.',
    })

    assert response.status_code == 200
    assert b'Please use your institute email' in response.data
    assert len(feedback_list) == 0


def test_reject_missing_email():
    client = app.test_client()
    response = client.post('/', data={
        'name': 'Aditya',
        'email': '',
        'course': 'Data Science',
        'feedback': 'The course was informative.',
    })

    assert response.status_code == 200
    assert b'All fields are required.' in response.data
    assert len(feedback_list) == 0
