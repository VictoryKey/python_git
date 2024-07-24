from flask import Flask, render_template, request, redirect, url_for, flash
import config

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == config.USERNAME and password == config.PASSWORD:
            flash('登录成功！')
            return redirect(url_for('success'))
        else:
            flash('用户名或密码错误！')
    return render_template('login.html')

@app.route('/success')
def success():
    return '登录成功，欢迎！'

if __name__ == '__main__':
    app.run(debug=True)
