#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template,request,url_for,send_from_directory,redirect
import os
from guestbook import *
from flask_dropzone import Dropzone
from datetime import datetime
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()+'/upload'
dropzone = Dropzone(app)
print os.getcwd()
photos_list = os.listdir(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    greeting_list = load_data()
    files_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files_list=files_list,greeting_list=greeting_list)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            print filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename, _external=True)
            return render_template('index.html') + file_url
    return render_template('index.html')





@app.route('/open/<filename>')
def open_file(filename):
    file_url = '/upload/'+filename
    return render_template('index.html')


@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = './upload/'+filename
    os.remove(file_path)
    files_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files_list=files_list)

@app.route('/post', methods=['POST'])
def post():
    """Comment's target url
    """
    comment = request.form.get('comment')
    create_at = datetime.now()

    save_data(comment, create_at)

    return redirect('/')

@app.route('/deletemsg/<msgindex>')
def delete_msg(msgindex):
    delete_data(msgindex)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)