import json
import os
import sys
import requests
from math import sqrt

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SECRET_KEY'] = "You can NEVER guess this LOL"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), 'wlysCraft\\data.db')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(app.root_path), 'wlysCraft\\uploadfiles')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.mkdir(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    from wlysCraft.models import User
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象

@app.route('/programs/zspd', methods=['POST'])
def zspd():
    try:
        num = int(request.form['num'])
    except:
        return json.dumps({'zsjg': ''}, ensure_ascii=False)
    if len(str(num)) > 10:
        return json.dumps({'zsjg': '太大了'}, ensure_ascii=False)
    if num > 1:
        if num == 2:
            return json.dumps({'zsjg': '是质数'}, ensure_ascii=False)
        if num % 2 == 0:
            return json.dumps({'zsjg': '是合数'}, ensure_ascii=False)

        for x in range(3, int(sqrt(num) + 1), 2):
            if num % x == 0:
                return json.dumps({'zsjg': '是合数'}, ensure_ascii=False)
        return json.dumps({'zsjg': '是质数'}, ensure_ascii=False)
    return json.dumps({'zsjg': '不是有效数字'}, ensure_ascii=False)


@app.route('/index/weather', methods=['POST'])
def weather():
    my_params = {'location': 'auto_ip',
                 'key': '216168dcbeeb4a9ba1dd70f153ac4463'}
    requesturl = "https://itsflicker.github.io/requestsAPI.html"
    url = "https://free-api.heweather.net/s6/weather/now"
    resn = requests.get(requesturl, params=my_params)
    url2 = "https://free-api.heweather.net/s6/weather/forecast"
    resf = requests.get(url2, my_params)
    messages = {'weathern': resn.json(), 'weatherf': resf.json()}
    return json.dumps(messages, ensure_ascii=False)


from wlysCraft import views, errors, commands

if __name__ == '__main__':
    app.run(debug=False, port=80, host="192.168.0.100")
