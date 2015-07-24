# -*- coding: utf-8 -*-
import tr
import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from flask import Flask


# create our little application :)
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():    
    text="""
    영어->한글 변환 https://ickyoung-photolog.appspot.com/etok/{english} <br>
    한글->영어 변환 https://ickyoung-photolog.appspot.com/ktoe/{한글} <br>    
    한글->영어 변환 https://ickyoung-photolog.appspot.com/trans/{한글or영어} <br> 
    """
    return text
@app.route('/trans/<eng_or_kor>')
def trans(eng_or_kor):
    return eng_or_kor + " -> " + tr.trans(eng_or_kor)

@app.route('/etok/<english>')
def etok(english):    
    return english + " -> " + tr.engTypeToKor(english)

@app.route('/ktoe/<korean>')
def ktoe(korean):    
    return korean + " -> " + tr.korTypeToEng(korean)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
