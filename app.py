from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedback_list = []
ALLOWED_EMAIL_DOMAIN = '@niet.co.in'


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        course = request.form.get('course', '').strip()
        feedback = request.form.get('feedback', '').strip()

        if not name or not email or not course or not feedback:
            error = 'All fields are required.'
        elif not email.endswith(ALLOWED_EMAIL_DOMAIN):
            error = 'Please use your institute email ending with @niet.co.in.'
        else:
            feedback_list.append({
                'name': name,
                'email': email,
                'course': course,
                'feedback': feedback,
            })
            return redirect(url_for('index'))

    return render_template('index.html', feedback_list=feedback_list, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
