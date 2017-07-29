# coding=utf-8

from flask import render_template
from app import app

import subprocess

@app.route('/')
def index():
    
    p = subprocess.Popen(["which", "python"], stdout=subprocess.PIPE).communicate()[0]

    return render_template('index.html',p = p)