#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-25
# Author: LXD
# 练习Flask的基本使用

from flask import Flask, url_for, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'path/uploads/'
# 创建一个Flask类的实例： WSGI 应用程序。
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 传参数1
@app.route('/user/<user_name>')
def show_user(user_name):
    return 'User: %s' % user_name

# 传参数2
@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'Post: %d' % post_id


# 构造URL
# with app.test_request_context():
#     print url_for('hello_world')
#     print url_for('show_user', user_name='test')
#     print url_for('show_post_id', post_id=123)
#     print url_for('hello_world', name='123')


# http方法
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST login'
    else:
        return 'GET login'


# 模板渲染
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


# 获取URL中提交的参数
@app.route('/argument')
def get_argument():
    search_word = request.args.get('wd', None)
    return render_template('argument.html', wd=search_word)


# 上传文件
@app.route('/upload/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload_file.html')

    else:
        file_name = request.form.get('filename', None)
        f = request.files.get('the_file', None)

        if file_name:
            if f:
                file_name = secure_filename(file_name)

                if os.path.exists(os.path.join(UPLOAD_FOLDER, file_name)):
                    return jsonify({
                        'code': 3,
                        'message': 'the filename exists',
                    }), 400

                f.save(os.path.join(UPLOAD_FOLDER, file_name))
                return jsonify({
                    'file_name': file_name,
                    'code': 0,
                    'message': 'success'
                }), 200

            else:
                return jsonify({
                    'code': 1,
                    'message': 'not upload file',
                }), 400

        else:
            return jsonify({
                'code': 2,
                'message': 'not set file name'
            }), 400


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)