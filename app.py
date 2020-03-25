from flask import Flask, render_template, request, redirect
from forms import LogInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'noam123'


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    result = {}
    if form.is_submitted():
        result = request.form
        if str(result["username"]) == 'noam' and str(result["password"]) == '1234':
            return render_template('User.html', result=result)
        else:
            return 'invalid username or password'
    return render_template('LogIn.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
