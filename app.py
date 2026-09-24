from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedback_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        course = request.form.get('course', '').strip()
        feedback = request.form.get('feedback', '').strip()

        if name and course and feedback:
            feedback_list.append({
                'name': name,
                'course': course,
                'feedback': feedback,
            })

        return redirect(url_for('index'))

    return render_template('index.html', feedback_list=feedback_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
