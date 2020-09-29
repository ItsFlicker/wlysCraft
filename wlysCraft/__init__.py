import json
import os
import requests
from math import sqrt

from flask import Flask, request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')


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
    url = "https://free-api.heweather.net/s6/weather/now"
    resn = requests.get(url, params=my_params)
    url2 = "https://free-api.heweather.net/s6/weather/forecast"
    resf = requests.get(url2, my_params)
    messages = {'weathern': resn.json(), 'weatherf': resf.json()}
    return json.dumps(messages, ensure_ascii=False)


from wlysCraft import views, errors

if __name__ == '__main__':
    app.run(debug=False, port=80, host="192.168.0.100")
