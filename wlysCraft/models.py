# -*- coding:utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from wlysCraft import db

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # id
    username = db.Column(db.String(20), nullable=False) # 用户名
    type = db.Column(db.String(20), nullable=False)  # 类型
    password_hash = db.Column(db.String(128)) # 密码

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

class Files(db.Model):
    __tablename__ = "files"
    filename = db.Column(db.String(32), primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    uploadtime = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    filedescribe = db.Column(db.String(64), nullable=False)

class Messages(db.Model):
    __tabname__ = "messages"
    message = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    sendtime = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)