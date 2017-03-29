import os
import pandas as pd
import numpy as np
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__) # create the application instance :)

app.config.from_object(__name__) # load config from this file , ds_app.py

app.config.update(dict(
    SECRET_KEY='development key'
))
app.config.from_envvar('DS_APP_SETTINGS', silent=True)

def get_classification_models():
    base = "https://docs.google.com/spreadsheets/d/"
    doc_id = "13uFW3lriigsAKJTAn_Ilo3fo7ZdeLUKbtqOe65Bf4iw"
    export_sheet = "/export?gid=261999384&format=csv"
    url = base + doc_id + export_sheet
    models = pd.read_csv(url,index_col=False)
    return models.to_dict(orient = "records")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metis_blog_0')
def metis_blog_0():
    return render_template('metis_0.html')

@app.route('/metis_blog_1')
def metis_blog_1():
    return render_template('metis_1.html')

@app.route('/metis_blog_2')
def metis_blog_2():
    classification_models = get_classification_models()
    return render_template('metis_2.html', cm=classification_models)

@app.route('/metis_blog_3')
def metis_blog_3():
    return render_template('metis_3.html')

@app.route('/metis_blog_4')
def metis_blog_4():
    return render_template('metis_4.html')

@app.route('/metis_blog_5')
def metis_blog_5():
    return render_template('metis_4.html')

