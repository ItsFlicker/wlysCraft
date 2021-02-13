from flask import render_template, request, url_for, redirect, flash, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os

from wlysCraft import app, db
from wlysCraft.models import User, Files


@app.route('/')
def main():
    return redirect('/index')

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/programs/')
def programs():
    return render_template("programs.html")

@app.route('/download/')
def download():
    return render_template("download.html", files=Files.query.all())

@app.route('/video/')
def video():
    return render_template("video.html")

@app.route('/messages/', methods=['GET', 'POST', 'DELETE'])
def messages():
    if request.method == 'POST':
        pass
    return render_template("messages.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.filter_by(username = username).first()

        if user == None:
            flash('Invalid username.')
            return redirect(url_for('login'))

        # 验证用户名和密码是否一致
        if user.validate_password(password):
            login_user(user)  # 登入用户
            flash('Login success.')
            return redirect(url_for('index'))  # 重定向到主页

        flash('Invalid password.')  # 如果验证失败，显示错误消息
        return redirect(url_for('login'))  # 重定向回登录页面

    return render_template("login.html")

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if not username or not password or not password2:
            flash('Invalid input.')
            return redirect(url_for('register'))

        if password != password2:
            flash('The two entered passwords do not match')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first() is not None:
            flash('用户名已存在!')
            return redirect(url_for('register'))

        user = User(username=username, type='User')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()  # 提交数据库会话

        flash('Register success.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/upload/', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files['file']
        describe = request.form['filedescribe']
        if not f or not describe:
            flash('Invalid input.')
            return redirect(url_for('upload'))

        if Files.query.get(f.filename) is not None:
            flash('文件名已存在!')
            return redirect(url_for('upload'))

        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        file = Files(filename=secure_filename(f.filename), username=current_user.username,
                     userid=current_user.id, filedescribe=describe)
        db.session.add(file)
        db.session.commit()

        flash('Upload success.')
        return redirect(url_for('download'))

    if current_user.type != 'Admin':
        flash('此功能暂不开放!')
        return redirect(url_for('download'))
    return render_template('upload.html')

@app.route('/download/downloadfile/<filename>')
def downloadfile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(filename), as_attachment=True)

@app.route('/download/deletefile/<filename>')
@login_required
def deletefile(filename):
    f = Files.query.get(filename)
    if current_user.type != 'Admin' and current_user.id != f.userid:
        flash('Sorry.But you have no permission to delete this file.')
        return redirect(url_for('download'))
    db.session.delete(f)
    db.session.commit()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))
    flash('删除成功')
    return redirect(url_for('download'))

@app.route('/settings/', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings.html')