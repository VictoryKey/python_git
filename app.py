from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import config

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# 只展示给用户的允许命令
shown_allowed_commands = ['ls', 'pwd', 'whoami', 'date']

# 实际上允许的命令（包括一些隐藏命令）
actual_allowed_commands = ['ls', 'pwd', 'whoami', 'date', 'cat', 'echo']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == config.USERNAME and password == config.PASSWORD:
            flash('登录成功！')
            return redirect(url_for('command'))
        else:
            flash('用户名或密码错误！')
    return render_template('login.html')

@app.route('/command', methods=['GET', 'POST'])
def command():
    result = ""
    if request.method == 'POST':
        command = request.form['command']
        # 过滤一些危险字符
        if any(char in command for char in [';', '|', '&', '`']):
            result = "命令包含非法字符！"
        else:
            command_name = command.split()[0]
            if command_name in actual_allowed_commands:
                try:
                    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result = result.stdout.decode('utf-8', errors='ignore') + result.stderr.decode('utf-8', errors='ignore')
                except Exception as e:
                    result = str(e)
            else:
                result = "命令不被允许"
    return render_template('command.html', result=result, allowed_commands=shown_allowed_commands)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
